import os
import shutil

# Defining file categories with their respective extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".pptx", ".txt"],
    "Music": [".mp3", ".wav", ".m4a", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".apk"],
    "Others": []
}

def organize_files(directory):
    # Check if the entered directory exists
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return
    
    # Create folders if they don't exist
    for category in file_categories.keys():
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    # Move files into respective folders
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_categories.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, category, file))
                    moved = True
                    break
            
            if not moved:  # If no category matched, move to 'Others'
                shutil.move(file_path, os.path.join(directory, "Others", file))

    print("Files have been organized successfully")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to organize: ")
    organize_files(folder_path)
