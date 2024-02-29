import unittest
from unittest.mock import patch
from stegcli import *

class TestStegCLI(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('builtins.print')
    def test_change_log(self, mock_print):
        # Test the change_log function
        LOGS = {
            "txt_path": 1,
            "img_path": 1,
            "audio_path": 1,
            "dest_path": 1,
            "msg": 1
        }
        change_log(LOGS=LOGS)
        mock_print.assert_called_with("(OK)-TEXT FILE IS SELECTED.\n\n(OK)-IMAGE FILE IS SELECTED.\n\n"
                                      "(OK)-AUDIO FILE IS SELECTED.\n\n(OK)-DEST FOLDER IS SELECTED.\n\n"
                                      "(OK)-MSG IS WRITTENED.\n\n")

    def test_get_error_embed(self):
        # Test the get_error function for embed mode
        global TEXT_PATH, IMAGE_PATH, AUDIO_PATH
        TEXT_PATH = "sample.txt"
        IMAGE_PATH = "image.jpg"
        AUDIO_PATH = "audio.wav"
        result = get_error("embed")
        self.assertEqual(result, 1)

    def test_get_error_extract(self):
        # Test the get_error function for extract mode
        global AUDIO_PATH
        AUDIO_PATH = "audio.wav"
        result = get_error("extract")
        self.assertEqual(result, 1)


    def test_select_audio_cmd_valid(self):
        # Test the select_audio_cmd function with a valid audio file
        global AUDIO_PATH
        AUDIO_PATH = "audio.wav"
        result = select_audio_cmd(AUDIO_PATH)
        self.assertFalse(result)
        self.assertEqual(LOGS["audio_path"], 0)

    def test_select_audio_cmd_invalid(self):
        # Test the select_audio_cmd function with an invalid audio file
        global AUDIO_PATH
        AUDIO_PATH = "invalid.txt"
        result = select_audio_cmd(AUDIO_PATH)
        self.assertFalse(result)
        self.assertEqual(LOGS["audio_path"], 0)


    @patch('builtins.print')
    def test_help(self, mock_print):
        # Test the help function
        help()
        mock_print.assert_called_with('usage: stegcli.py [-h] [-t text file] [-i image file] [-a audio file] [-d destination folder] [-m message]\n\n        optional arguments:\n        -h, --help     show this help message and exit\n        ')

    @patch('stegcli.embed_cmd')
    def test_main_embed(self, mock_embed_cmd):
        # Test the main function with embed mode
        with patch('sys.argv', ['stegcli.py', '-i', 'image.jpg', '-t', 'sample.txt','-em']):
            main()
            mock_embed_cmd.assert_called_once()

    @patch('stegcli.extract_cmd')
    def test_main_extract(self, mock_extract_cmd):
        # Test the main function with extract mode
        with patch('sys.argv', ['stegcli.py', '-i', 'image.jpg', '-ex']):
            main()
            mock_extract_cmd.assert_called_once()

    @patch('builtins.print')
    def test_main_no_mode(self, mock_print):
        # Test the main function with no mode specified
        with patch('sys.argv', ['stegcli.py']):
            main()
            mock_print.assert_called_with("Please specify a mode (embed/extract)")

if __name__ == '__main__':
    unittest.main()
