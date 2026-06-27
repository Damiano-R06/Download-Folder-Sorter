from pathlib import Path
import shutil

downloads = Path.home() / "Downloads"

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "PDFs": [".pdf"],
    "Docs": [".docx"],
    "TextFiles": [".txt"],
    "Videos": [".mp4", ".mov"],
    "Zips": [".zip"],
    "Audio": [".mp3"],
    "Code": [".py", ".java", ".html", ".c", ".json"],
}

def get_category(suffix):
    for folder_name, extensions in CATEGORIES.items():
        if suffix in extensions:
            return folder_name
    return "Other"
        
for item in downloads.iterdir():
    if item.is_file():
        category = get_category(item.suffix.lower())
        destination_folder = downloads / category
        destination_folder.mkdir(exist_ok = True) #Creates folder if needed
        shutil.move(str(item), destination_folder / item.name)