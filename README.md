# Background Remover GUI (Python + Tkinter + Rembg)

A simple drag-and-drop GUI for removing image backgrounds using the [rembg](https://github.com/danielgatis/rembg) library.  
Built with Python's Tkinter and `tkinterdnd2` for drag-and-drop support.

---

## Features
- **Drag & Drop** an image directly onto the window.
- **Remove Background** using AI (powered by `rembg`).
- **Preview Output** before saving.
- **Save Result** as PNG (with transparent background).
- **Preserves Original Resolution** (no quality loss).

---

## Requirements
- Python **3.8 or higher** (https://www.python.org/)
- pip (comes with Python)

---

## Installation

1. **Clone or download this repository**  
   ```bash
   git clone https://github.com/NeilAdrian-0423/rembg_ui.git
   cd rembg-gui
2. **Make a virtual env**
```bash
   python -m venv venv or python3 -m venv venv 
```
3. **Activate virtual environment**
   - **Windows (Command Prompt/Powershell):**
   ```cmd
   .\venv\Scripts\activate
   ```
   - **Linux:**
    ```bash
    source venv/bin/activate

4. **Install dependencies**
   ```cmd
      pip install rembg pillow tkinterdnd2
   ```

## Run

python rembg_gui.py or python3 rembg_gui.py