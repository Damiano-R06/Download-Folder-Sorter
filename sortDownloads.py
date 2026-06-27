from pathlib import Path
import shutil

downloads = Path.home() / "Downloads"

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ",png", ".gif", "webp"],
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
        

            