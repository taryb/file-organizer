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



---

### 📄 `LICENSE` (MIT License)
Create a new file named `LICENSE` in the root. Contents:

```text
MIT License

Copyright (c) 2025 Tary B.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
