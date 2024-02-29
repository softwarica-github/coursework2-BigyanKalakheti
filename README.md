# Steganography Tool
This Python-based Steganography Tool provides a graphical user interface (GUI) for hiding and extracting data within images and audio files. It utilizes the Tkinter library for the GUI, PIL (Pillow) for image processing, and various other libraries for audio and file handling.

## Features
Embedding Data:

Embeds text data into images.
Embeds text data into audio files (requires a valid audio file).
Extracting Data:

Extracts hidden text data from images.
Extracts hidden text data from audio files.

## Installation
Ensure you have the required dependencies installed:

```bash
pip install pillow
```
### Usage
Run the GUI application using the provided steg_gui.py file:
```bash
python main.py
```
The GUI provides options to select text files, image files, audio files, and destination folders. Additionally, you can enter a message for embedding.

Use the buttons to perform the following actions:

Reset: Reset all selected paths.
Embed Data: Start the embedding process.
Extract Data: Start the extraction process.
View the status log for information about the selected paths and any errors.

## Command-Line Interface (CLI)
The tool also offers a command-line interface for batch processing. Use the stegcli.py script with the following options:

```bash
python stegcli.py -h  # Display help message
python stegcli.py  -a <audio_file> -d <destination_folder> -m <message> -em  # Embed data
python stegcli.py  -a <audio_file> -d <destination_folder> -ex  # Extract data
```
## Examples

### Embedding Data
```bash
python stegcli.py -t text.txt -i image.jpg -d output_folder -em
```

### Extracting Data
```bash
python stegcli.py -i embedded.jpg  -d output_folder -ex
```
## Disclaimer
This tool is for educational and research purposes only. Use responsibly and respect privacy laws.

## Contributors
[Bigyan Kalakheti]

Youtube Link : https://youtu.be/DFWIMdT-loo?si=AMYcaqdDnBR9E3ZG

Feel free to contribute to this project by opening issues or submitting pull requests.
