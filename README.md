<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,50:0F766E,100:0B1220&height=190&section=header&text=Python%20GUI%20Calculator&fontSize=42&fontColor=F1F5F9&fontAlignY=38&animation=fadeIn&desc=A%20lightweight%20Tkinter%20calculator%20with%20keyboard%20support%20and%20expression%20preview&descAlignY=61&descSize=15" alt="Python GUI Calculator animated project banner" width="100%" />
</p>
<h1 align="center">Python GUI Calculator</h1>


A sleek, fully-functional desktop calculator built with Python and Tkinter — no external dependencies required.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

---

## ✨ Features

- **Basic Arithmetic** — Addition, Subtraction, Multiplication, Division
- **Utility Functions** — Toggle sign (±), Percentage (%), Clear (C)
- **Live Expression Preview** — Shows the full expression above the main display
- **Keyboard Support** — Use your keyboard for digits, operators, Enter, and Backspace
- **Zero Division Handling** — Friendly error message instead of crashing
- **Dark UI** — Eye-friendly dark theme with color-coded button groups
- **No External Libraries** — Runs on any Python 3 installation out of the box

---

## 📸 Preview

```
┌──────────────────────────────────┐
│                    9 × 12 =      │
│                         108      │
├──────┬──────┬──────┬─────────────┤
│  C   │  ±   │  %   │      ÷      │
├──────┼──────┼──────┼─────────────┤
│  7   │  8   │  9   │      ×      │
├──────┼──────┼──────┼─────────────┤
│  4   │  5   │  6   │      −      │
├──────┼──────┼──────┼─────────────┤
│  1   │  2   │  3   │      +      │
├────────────┬──────┬──────────────┤
│     0      │  .   │      =       │
└────────────┴──────┴──────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.7 or higher** installed on your system
- `tkinter` (bundled with the standard Python installer on Windows and macOS; see below for Linux)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/tracolerd/A-Simple-Calculator-Using-Python.git

# 2. Navigate into the project directory
cd A-Simple-Calculator-Using-Python
```

> **No `pip install` needed** — this project uses only the Python standard library.

### Linux users — install Tkinter if missing

```bash
# Debian / Ubuntu
sudo apt-get install python3-tk

# Fedora / RHEL
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

---

## ▶️ Running the Calculator

```bash
python calculator.py
```

or, if your system defaults to Python 2:

```bash
python3 calculator.py
```

The calculator window will open immediately — no configuration needed.

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0` – `9` | Input digits |
| `.` | Decimal point |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `Enter` or `Return` | Evaluate (`=`) |
| `Backspace` or `Esc` or `c` | Clear |

---

## 📁 Project Structure

```
python-gui-calculator/
│
├── calculator.py   # Main application — all code lives here
└── README.md       # You are here
```

---

## 🛠️ How It Works

| Layer | Detail |
|---|---|
| **GUI Framework** | `tkinter` (Python's built-in UI toolkit) |
| **Layout** | `grid` geometry manager for the button pad; `pack` for the display |
| **Expression Evaluation** | Operator tokens are accumulated into a string; on `=` it is evaluated with Python's `eval()` after replacing display symbols (`÷ × −`) with Python operators |
| **Keyboard Events** | Bound via `root.bind("<Key>", ...)` and mapped to the same handler as mouse clicks |

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!

1. **Fork** the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a **Pull Request**

---
---

## Creator, Developer & Maintainer

**Created, designed, developed, and maintained by [Nurul Faiyaz](https://github.com/tracolerd).**

This project is independently built and maintained by Nurul Faiyaz. The project's design, implementation, and documentation are his work.

<p align="center">
  <a href="https://www.facebook.com/faiyaz.888"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook" /></a>
  <a href="https://www.instagram.com/tracolerd"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" /></a>
  <a href="https://www.linkedin.com/in/faiyaz-xyz"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://x.com/faiyaz_explores"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X" /></a>
  <a href="https://github.com/tracolerd"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="mailto:scrollfaiyaz@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://nurul-faiyaz.netlify.app/"><img src="https://img.shields.io/badge/Portfolio-Visit%20Website-0F766E?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Personal website" /></a>
</p>

<p align="center">
  <a href="https://www.facebook.com/faiyaz.888">Facebook</a> ·
  <a href="https://www.instagram.com/tracolerd">Instagram</a> ·
  <a href="https://www.linkedin.com/in/faiyaz-xyz">LinkedIn</a> ·
  <a href="https://x.com/faiyaz_explores">X / Twitter</a> ·
  <a href="https://github.com/tracolerd">GitHub</a> ·
  <a href="mailto:scrollfaiyaz@gmail.com">Email</a> ·
  <a href="https://nurul-faiyaz.netlify.app/">Website</a>
</p>

## 📝 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---