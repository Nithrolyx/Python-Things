import os
import shutil

def organize_files(directory_path):
    # Define file types and corresponding folder names
    file_types = {
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".pdf": "Documents",
        ".docx": "Documents",
        ".mp4": "Videos",
        ".txt": "TextFiles",
        ".zip": "Zip Files",
        ".rar": "Rar Files",
        ".7z": "Zip Files",
        # Add more file types as needed
    }

    # Create folders if not exist
    for folder in file_types.values(): 
        folder_path = os.path.join(directory_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Organize files
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lower()

            # Check if the file type is in our dictionary
            if file_extension in file_types:
                destination_folder = file_types[file_extension]
                destination_path = os.path.join(directory_path, destination_folder, filename)

                # Move the file to the appropriate folder
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {destination_folder} folder.")

if __name__ == "__main__":
    # Get the directory path from the user
    directory_path = input("Enter the directory path to organize: ")

    # Check if the directory exists
    if os.path.exists(directory_path):
        organize_files(directory_path)
        print("Organizing complete.")
    else:
        print("Directory does not exist. Please provide a valid directory path.")
