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

for item in downloads.iterdir():
    if item.is_file():
        print(item.name, "->", item.suffix)