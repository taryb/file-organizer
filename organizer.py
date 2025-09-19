#!/usr/bin/env python3
"""
organizer.py - A simple file organizer demo for portfolio use.
"""

import sys
import os
import shutil
from pathlib import Path

# Define some default categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".md"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Scripts": [".py", ".sh", ".bat"],
}


def organize(directory: str):
    """Organize files in the given directory into subfolders."""
    path = Path(directory).expanduser().resolve()

    if not path.exists() or not path.is_dir():
        print(f"❌ Error: {directory} is not a valid directory.")
        return

    print(f"📂 Organizing files in: {path}")

    for file in path.iterdir():
        if file.is_file():
            moved = False
            for category, extensions in CATEGORIES.items():
                if file.suffix.lower() in extensions:
                    target_dir = path / category
                    target_dir.mkdir(exist_ok=True)
                    shutil.move(str(file), str(target_dir / file.name))
                    print(f"  ✅ Moved {file.name} → {category}/")
                    moved = True
                    break
            if not moved:
                # Put uncategorized files in "Other"
                other_dir = path / "Other"
                other_dir.mkdir(exist_ok=True)
                shutil.move(str(file), str(other_dir / file.name))
                print(f"  ➡️  Moved {file.name} → Other/")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python organizer.py <directory>")
    else:
        organize(sys.argv[1])
