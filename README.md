<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,50:0F766E,100:0B1220&height=190&section=header&text=Python%20GUI%20Calculator&fontSize=42&fontColor=F1F5F9&fontAlignY=38&animation=fadeIn&desc=A%20lightweight%20Tkinter%20calculator%20with%20keyboard%20support%20and%20expression%20preview&descAlignY=61&descSize=15" alt="Python GUI Calculator animated project banner" width="100%" />
</p>

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

## 📝 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

## 👤 Author

Made by Faiyaz using Python

> *"Any sufficiently advanced calculator is indistinguishable from magic."*

---

## Author & Development

**Project author and solo developer:** [Nurul Faiyaz](https://github.com/tracolerd).

This project is independently developed and maintained by Nurul Faiyaz. AI-assisted tools may be used as part of the development workflow; the project author remains responsible for technical decisions, code review, validation, and maintenance.

