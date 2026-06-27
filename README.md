# Downloads Folder Organizer

A simple Python script that automatically sorts your Downloads folder into categorized subfolders.

## What It Does

Scans your Downloads folder and moves files into organized subfolders based on file type:

| Folder | File Types |
|--------|-----------|
| Images | `.jpg` `.jpeg` `.png` `.gif` `.webp` |
| PDFs | `.pdf` |
| Docs | `.docx` |
| TextFiles | `.txt` |
| Videos | `.mp4` `.mov` |
| Zips | `.zip` |
| Audio | `.mp3` |
| Code | `.py` `.java` `.html` `.c` `.json` |
| Other | Everything else |

## Requirements

- Python 3.x
- No external dependencies — uses only the standard library (`pathlib`, `shutil`)

## Usage

```bash
python organizer.py
```

> **Note:** The script targets your system's Downloads folder automatically (`~/Downloads`). Back up any important files before running.

## Adding More File Types

To support additional extensions, add them to the `CATEGORIES` dictionary in the script:
