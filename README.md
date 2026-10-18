<p align="center">
  <img src="assets/readme-hero.svg" alt="Python GUI Calculator — custom animated project banner" width="100%" />
</p>

<h1 align="center">Python GUI Calculator</h1>

<p align="center">
  <strong>A compact desktop calculator, built for fast and intuitive input.</strong><br/>
  A Python and Tkinter calculator with live expression preview, keyboard support and friendly division-by-zero handling.
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-Desktop_app-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="Python — Desktop app" /></a>
  <a href="https://docs.python.org/3/library/tkinter.html"><img src="https://img.shields.io/badge/Tkinter-GUI-0F766E?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="Tkinter — GUI" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/MIT-License-16A34A?style=for-the-badge&amp;logo=opensourceinitiative&amp;logoColor=white" alt="MIT — License" /></a>
</p>

<p align="center">
  <a href="#project-details">Project details</a> · <a href="#project-setup">Get started</a> · <a href="#project-architecture">How it works</a> · <a href="#creator-developer-maintainer">Creator</a>
</p>

---

<a id="project-details"></a>
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

<a id="project-setup"></a>
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

<a id="project-architecture"></a>
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

## 📝 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

---

## Creator, Developer & Maintainer

**Created, designed, developed, documented, and maintained independently by [Nurul Faiyaz](https://github.com/tracolerd).**

<p align="center">
  <a href="https://www.facebook.com/faiyaz.888"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&amp;logo=facebook&amp;logoColor=white" alt="Facebook" /></a>
  <a href="https://www.instagram.com/tracolerd"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&amp;logo=instagram&amp;logoColor=white" alt="Instagram" /></a>
  <a href="https://www.linkedin.com/in/faiyaz-xyz"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&amp;logo=linkedin&amp;logoColor=white" alt="LinkedIn" /></a>
  <a href="https://x.com/faiyaz_explores"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&amp;logo=x&amp;logoColor=white" alt="X" /></a>
  <a href="https://github.com/tracolerd"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="GitHub" /></a>
  <a href="mailto:scrollfaiyaz@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&amp;logo=gmail&amp;logoColor=white" alt="Email" /></a>
  <a href="https://nurul-faiyaz.netlify.app/"><img src="https://img.shields.io/badge/Portfolio-Visit%20Website-0F766E?style=for-the-badge&amp;logo=googlechrome&amp;logoColor=white" alt="Website" /></a>
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

## License

See [LICENSE](LICENSE) for the license terms.
