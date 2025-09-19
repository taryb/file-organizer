# Organizer

A simple Python CLI tool to automatically sort and organize files into folders by type  
(e.g. Documents, Images, Videos, Archives). Helps keep your Downloads folder tidy.

## Features
- Organize files by extension (e.g. `.jpg`, `.pdf`, `.zip`)
- Automatically create folders if they don’t exist
- Safe mode (preview actions without moving files)

## Roadmap
- [ ] Add config file for custom rules
- [ ] Support recursive folder scanning
- [ ] Add GUI with PyQt5
- [ ] Optional auto-run on startup

## Quick Start
```bash
git clone https://github.com/<your-username>/organizer.git
cd organizer
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python organizer.py
