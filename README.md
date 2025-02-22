# Desktop Organizer
A simple *Python-based* script to automatically organize files in a directory by categorizing them into folders based on their file types.

## Features
* Automatically sorts files into predefined categories (Images, Videos, Documents, Music, Archives, Executables, Others).
* Creates category folders if they do not exist.
* Moves unclassified files into an "Others" folder.
* Simple and easy-to-use command-line interface.

## Installation
### Prerequisites
Make sure you have *Python* installed. You can download it from [here](python.org).
### Clone the Repository
```
git clone https://github.com/prizzansh/desktop-organizer.git
cd desktop-organizer
```

## Usage
Run the script using:
```
python organizer.py
```
Then enter the *path* of the folder you want to organize when prompted.
### Example
```
Enter the path of the folder to organize: C:\Users\username\Desktop
```
This will sort all files on the Desktop into respective folders.

## File Categories
The script categorizes files into the following folders:
* Images (.jpg, .jpeg, .png, .gif, .bmp, .svg)
* Videos (.mp4, .mkv, .mov, .avi, .flv)
* Documents (.pdf, .docx, .doc, .xlsx, .pptx, .txt)
* Music (.mp3, .wav, .m4a, .aac, .flac)
* Archives (.zip, .rar, .tar, .gz, .7z)
* Executables (.exe, .msi, .bat, .sh, .apk)
* Others (Any file that does not match the above categories)
### You can add more file types according to specific needs
