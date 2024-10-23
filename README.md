# File Organizer Script

This Python script organizes files in a directory into subfolders based on their file types. It categorizes files by their extensions (e.g., `.txt`, `.jpg`, `.pdf`, etc.) and moves them into corresponding folders (e.g., "Text Files", "Images", "PDF Documents").

## Features

- Automatically organizes files by file type.
- Supports a variety of file types such as text files, images, audio, video, compressed files, and more.
- Creates folders if they do not exist.
- Uses `glob` to search for files based on their extensions.
- Efficiently moves files to their respective folders.

## Supported File Types

| File Extension | Folder Name         |
| -------------- | ------------------- |
| `.txt`         | Text Files           |
| `.docs`        | Word Documents       |
| `.pdf`         | PDF Documents        |
| `.jpg`         | Images               |
| `.jpeg`        | Images               |
| `.png`         | Images               |
| `.bmp`         | Images               |
| `.xlsx`        | Spread Sheets        |
| `.pptx`        | Presentations        |
| `.mp3`         | Audio                |
| `.mp4`         | Videos               |
| `.zip`         | Compressed Files     |

## Prerequisites

- Python 3.x
- `shutil` and `glob` (included in the Python standard library)

## Installation

1. Clone or download this repository.
2. Navigate to the directory where the script is located.
3. Ensure Python 3.x is installed on your system.

## Usage

1. Open your terminal (or command prompt).
2. Run the script and provide the path to the directory you want to organize:

```bash
python organize_files.py
Enter the full path to the folder that contains the files to organize.
The script will automatically move the files into appropriate folders based on their file extensions.
Example
If your directory contains the following files:

example/
├── document.txt
├── image.jpg
├── spreadsheet.xlsx
├── video.mp4
After running the script, the directory will be organized like this:

example/
├── Text Files/
│   └── document.txt
├── Images/
│   └── image.jpg
├── Spread Sheets/
│   └── spreadsheet.xlsx
├── Videos/
│   └── video.mp4
Contributing
Contributions are welcome! Please submit a pull request or open an issue if you'd like to contribute.