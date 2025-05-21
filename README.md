# Haidar Dagham's Snake Game 🐍🎮

A fun and beginner-friendly **Snake Game** built with Python and Tkinter. This game features a clean design, easy controls, and wrap-around screen behavior — perfect for casual play and learning GUI development.

## 🖥 Features

- Colorful and responsive GUI built with Tkinter  
- Arrow key controls for smooth snake movement  
- Real-time scoring system  
- Restart button after game over  
- Border wrap-around mechanics  
- Built-in collision detection  
- Packaged as a standalone `.exe` using PyInstaller

---

## 🚀 Running the Game

### 🐍 From Source (Python Script)

Ensure Python is installed, then run:

```bash
python snake_game-easy.py
```

Use your keyboard arrow keys to control the snake!

### 📦 As Executable (Windows .exe)

If you've downloaded the `.exe` version:

Just double-click on `snake_game-easy.exe` to play.  
No Python installation required.

---

## 🛠 How It Was Built

- **Language:** Python 3  
- **GUI Framework:** Tkinter  
- **Randomization:** Python’s `random` module  
- **Packaging Tool:** PyInstaller

### 🛠 To generate the `.exe` file yourself:

1. Place `snake_game-easy.py` and `icon.ico` in the same folder.  
2. Open a terminal in that folder.  
3. Run:

```bash
pyinstaller -F -w -i icon.ico snake_game-easy.py
```

This will create an executable in the `/dist` directory.

---

## 📁 Files Included

- `snake_game-easy.py` – The main Python script  
- `snake_game-easy.exe` – The compiled Windows executable  
- `icon.ico` – Icon image for the game window  
- `README.md` – This file

---

## 👨‍💻 Author

**Haidar Dagham**
