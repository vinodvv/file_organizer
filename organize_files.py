import os
import glob
import shutil


def organize_files(directory):
    """
    Organizes files in the given directory into folders based on their file extensions.

    Args:
        directory (str): The path of the directory containing the files to organize.

    This function creates folders based on file types (like 'Text Files', 'Images', etc.)
    and moves the corresponding files into these folders. Files with extensions not listed
    in the `file_types` dictionary are ignored.
    """

    # Dictionary mapping file extensions to folder names
    file_types = {
        ".txt": "Text Files",
        ".docx": "Word Document",
        ".pdf": "PDF Document",
        ".jpg": "Images",
        ".png": "Images",
        ".xlsx": "Spread Sheet",
        ".jpeg": "Images",
        ".bmp": "Images",
        ".pptx": "Presentation",
        ".mp3": "Audio",
        ".mp4": "Video",
        ".zip": "Compressed Files"
    }

    # Iterate over each file type and its corresponding folder
    for file_types, folder_name in file_types.items():
        # Create the folder path inside the directory
        folder_path = os.path.join(directory, folder_name)

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        # Use glob to find all files with the current extension
        for file in glob.glob(f"{directory}/*{file_types}"):
            # Move each file to corresponding folder
            shutil.move(file, folder_path)
            print(f"Moved {os.path.basename(file)} to {folder_name}")


if __name__ == "__main__":
    # Prompt user to enter the directory path to organize
    directory_to_organize = input("Enter the directory to organize: ")

    # Organize the files in the specified directory
    organize_files(directory_to_organize)
