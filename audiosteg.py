import os
import wave
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('-f', help='Select Audio File', dest='audiofile')
# parser.add_argument('-m', help='Enter your Secret Message', dest='secretmsg')
# parser.add_argument('-o', help='Your Output file path and name', dest='outputfile')
# parser.add_argument('-e', help='extract file', dest='extractfile')
# args = parser.parse_args()
# af = args.audiofile
# string = args.secretmsg
# output = args.outputfile
# arged = False

# def help():
#   print("\033[92mHide Your Secret Message in Audio Wave File.\033[0m")
#   print ('''usage: audiosteg.py [-h] [-f AUDIOFILE] [-m SECRETMSG] [-o OUTPUTFILE]

# optional arguments:
#   -h, --help    show this help message and exit
#   -f AUDIOFILE  Select Audio File
#   -m SECRETMSG  Enter your message
#   -o OUTPUTFILE Your output file path and name''')

def em_audio(af, string, output):
      print ("Please wait...")
      waveaudio = wave.open(af, mode='rb')
      frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
      string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
      bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
      for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
      frame_modified = bytes(frame_bytes)
      with wave.open(output, 'wb') as fd:
        fd.setparams(waveaudio.getparams())
        fd.writeframes(frame_modified)
      waveaudio.close()
      print ("Done...")

def ex_msg(ae):
        print ("Please wait...")
        waveaudio = wave.open(ae, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        msg = string.split("###")[0]
        print("Your Secret Message is: \033[1;91m"+msg+"\033[0m")
        waveaudio.close()
        return msg


# try:
#   if af and string and output:
#       arged = True
#       em_audio(af, string, output)
#   if  args.extractfile:
#       arged = True 
#       ex_msg(args.extractfile)
# except:
#   print ("Something went wrong!! try again")
#   quit('')
