import os
import shutil
from pathlib import Path

def GTF():
    folder = input("Enter the full path of the folder you want to organze: ")
    if not os.path.exists(folder):
        print("The folder does not exist")
        return None
    return folder 

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif','.raw'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.log', '.asc', '.asy'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Compressed': ['.zip', '.rar', '.7z'],
    'Installers': ['.exe', '.msi'],
    'Code': ['.py', '.js', '.cpp', '.html'],
}

def organize(folder):
    folder = Path(folder)

    for file in folder.iterdir():
        if file.is_file():
            moved = False
            for folder_name, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    target_dir = folder / folder_name 
                    target_dir.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target_dir / file.name))
                    moved = True
                    break

    if not moved:
        others_dir = folder / 'Others'
        others_dir.mkdir(exist_ok=True)
        shutil.move(str(file), str(others_dir / file.name))
        

def main():
    folder = GTF()
    if folder:
        organize(folder)
        print("Organized files successfully")

if __name__ == "__main__":
    main()
 