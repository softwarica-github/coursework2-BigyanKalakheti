import argparse
import threading
from img_stg import ImgStg
from audiosteg import *
from utils import compatible_path
import os

# Global variables
DIR_PATH = compatible_path(os.path.dirname(os.path.realpath(__file__)))
TEXT_PATH = ""
IMAGE_PATH = ""
AUDIO_PATH = ""
ERROR = ""
STG = ImgStg()
global LOGS

LOGS = {
    "img_path": 0,
    "txt_path": 0,
    "dest_path": 0,
    "audio_path": 0,
    "msg": 0
}

# Function to change log
def change_log(reset=False, LOGS=None):
    text_log = ""

    if reset is False:
        # TEXT PATH
        if LOGS["txt_path"] == 0:
            text_log += "(?)-TEXT FILE IS NOT SELECTED!(not required for data extraction)\n\n"
        else:
            text_log += "(OK)-TEXT FILE IS SELECTED.\n\n"
        # IMAGE PATH
        if LOGS["img_path"] == 0:
            text_log += "(?)-IMAGE FILE IS NOT SELECTED!\n\n"
        else:
            text_log += "(OK)-IMAGE FILE IS SELECTED.\n\n"
        # AUDIO PATH
        if LOGS["audio_path"] == 0:
            text_log += "(?)-AUDIO FILE IS NOT SELECTED!(required only for audio steganography)\n\n"
        else:
            text_log += "(OK)-AUDIO FILE IS SELECTED.\n\n"
        # DESTINATION PATH
        if LOGS["dest_path"] == 0:
            text_log += "(?)-DEST FOLDER IS NOT SELECTED!\n\n"
        else:
            text_log += "(OK)-DEST FOLDER IS SELECTED.\n\n"
        if LOGS["msg"] == 0:
            text_log += "(?)-MSG IS NOT WRITTEN!(required for audio steg)\n\n"
        else:
            text_log += "(OK)-MSG IS WRITTENED.\n\n"

    print(text_log)


# Function to handle errors
def get_error(mode="embed"):
    """
    This function checks if the required paths are selected.
    and returns 0 if there is no error.
    """
    if mode == "embed":  # if embed is selected
        if AUDIO_PATH:
            return 0
        if not TEXT_PATH:
            print("INFO: TEXT PATH IS NOT SELECTED!")
            return 1
    elif mode == "extract":  # if extract is selected
        if AUDIO_PATH:
            return 0
    if not IMAGE_PATH:
        print("INFO: IMAGE PATH IS NOT SELECTED!")
        return 1

    return 0


# Function to select text file
def select_text_cmd():
    if "txt" != TEXT_PATH[len(TEXT_PATH)-3:]:
        TEXT_PATH = ""
        return False
    else:
        LOGS["txt_path"] = 1
    change_log()

# Function to select image file
def select_img_cmd():
    if "jpg" != IMAGE_PATH[len(IMAGE_PATH)-3:]:
        IMAGE_PATH = ""
        return False
    else:
        LOGS["img_path"] = 1
    change_log()

# Function to select audio file
def select_audio_cmd(AUDIO_PATH):
    if ("wav" != AUDIO_PATH[len(AUDIO_PATH)-3:]) or ("mp3" != AUDIO_PATH[len(AUDIO_PATH)-3:]) :
        print("Selected file is not a valid audio file.")
        AUDIO_PATH = ""  # Reset the audio file path
        return False
    else:
        LOGS["audio_path"] = 1
    change_log()

# Function to select destination folder
def select_dest_cmd():
    LOGS["dest_path"] = 1
    change_log()

# Function to embed data
def embed_cmd():
    """
    this function starts the embedding process.
    """
    if get_error("embed") == 0 and AUDIO_PATH and msg:
            if not select_audio_cmd(AUDIO_PATH):
                threading.Thread(target=em_audio, args=(AUDIO_PATH,msg,DEST_PATH+"/steg.wav")).start()

    elif get_error("embed") == 0 and IMAGE_PATH and TEXT_PATH :
        print(f"text: {TEXT_PATH}, image: {IMAGE_PATH}, dest: {DEST_PATH}")
        text = fileHandler.read(TEXT_PATH)
        print(text,IMAGE_PATH)
        threading.Thread(target=STG._merge_txt, args=(IMAGE_PATH,TEXT_PATH,DEST_PATH)).start()
# Function to extract data
def extract_cmd():
    """
    this function starts the extraction process.
    """
    if get_error("extract") == 0 and AUDIO_PATH:
            result_queue = Queue()
            def ex_msg_wrapper(audio_path):
                result = ex_msg(audio_path)
                result_queue.put(result)
            # Start the thread
            thread = threading.Thread(target=ex_msg_wrapper, args=(AUDIO_PATH,))
            thread.start()

            thread.join()

            # Retrieve the result from the Queue
            result = result_queue.get()
    elif get_error("extract") == 0:
        threading.Thread(target=STG._unmerge_txt, args=(IMAGE_PATH, DEST_PATH)).start()

def help():
        print("\033[92mSteganography CLI TOOL\033[0m")
        print ('''usage: stegcli.py [-h] [-t text file] [-i image file] [-a audio file] [-d destination folder] [-m message]

        optional arguments:
        -h, --help     show this help message and exit
        ''')

# Parse command-line arguments
def main():
    parser = argparse.ArgumentParser(description='Steganography CLI Tool')
    parser.add_argument('-t','--text', help='Path to the text file')
    parser.add_argument('-i','--image', help='Path to the image file')
    parser.add_argument('-a','--audio', help='Path to the audio file')
    parser.add_argument('-d','--dest', help='Path to the destination folder')
    parser.add_argument('-m','--msg', help='Message for embedding/extraction')
    parser.add_argument('-em','--embed', help='embedding',action="store_true")
    parser.add_argument('-ex','--extract', help='extraction',action="store_true")
    args = parser.parse_args()
    arged = False

    if not arged:
        help()        

    global IMAGE_PATH
    IMAGE_PATH = args.image
    global AUDIO_PATH
    AUDIO_PATH = args.audio
    global TEXT_PATH
    TEXT_PATH = args.text
    global DEST_PATH
    DEST_PATH = args.dest
    if DEST_PATH is None:
        DEST_PATH = DIR_PATH
    global msg
    msg = args.msg
    if args.embed:
        embed_cmd()
    elif args.extract:
        extract_cmd()
    else:
        print("Please specify a mode (embed/extract)")    
    
if __name__ == "__main__":
    main()