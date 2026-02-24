import os
import shutil

folder_path = r"C:\Users\Panagiotis\Desktop\Demo"

file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".csv", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}

for folder in file_types.keys():
    folder_full_path = os.path.join(folder_path, folder)
    if not os.path.exists(folder_full_path):
        os.makedirs(folder_full_path)

for file in os.listdir(folder_path):
    file_full_path = os.path.join(folder_path, file)
    if os.path.isfile(file_full_path):
        for folder, extensions in file_types.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(file_full_path, os.path.join(folder_path, folder, file))
                break

print("The folder has been organized magically! ✨")