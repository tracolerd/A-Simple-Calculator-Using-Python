import tkinter as tk
from tkinter import font
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("380x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a2e")

        self.expression = ""
        self.display_var = tk.StringVar(value="0")
        self.sub_display_var = tk.StringVar(value="")
        self.new_number = True

        self._build_ui()

    def _build_ui(self):
        # ── Display Frame ──────────────────────────────────────────────
        display_frame = tk.Frame(self.root, bg="#16213e", pady=10)
        display_frame.pack(fill="x", padx=10, pady=(15, 5))

        sub_lbl = tk.Label(
            display_frame,
            textvariable=self.sub_display_var,
            bg="#16213e",
            fg="#6c7a9c",
            font=("Courier New", 13),
            anchor="e",
        )
        sub_lbl.pack(fill="x", padx=12)

        main_lbl = tk.Label(
            display_frame,
            textvariable=self.display_var,
            bg="#16213e",
            fg="#e2e8f0",
            font=("Courier New", 38, "bold"),
            anchor="e",
        )
        main_lbl.pack(fill="x", padx=12)

        # ── Button Grid ────────────────────────────────────────────────
        btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        btn_frame.pack(fill="both", expand=True, padx=10, pady=10)

        #  (label, row, col, colspan, style)
        buttons = [
            ("C",   0, 0, 1, "clear"),
            ("±",   0, 1, 1, "func"),
            ("%",   0, 2, 1, "func"),
            ("÷",   0, 3, 1, "op"),

            ("7",   1, 0, 1, "num"),
            ("8",   1, 1, 1, "num"),
            ("9",   1, 2, 1, "num"),
            ("×",   1, 3, 1, "op"),

            ("4",   2, 0, 1, "num"),
            ("5",   2, 1, 1, "num"),
            ("6",   2, 2, 1, "num"),
            ("−",   2, 3, 1, "op"),

            ("1",   3, 0, 1, "num"),
            ("2",   3, 1, 1, "num"),
            ("3",   3, 2, 1, "num"),
            ("+",   3, 3, 1, "op"),

            ("0",   4, 0, 2, "num"),
            (".",   4, 2, 1, "num"),
            ("=",   4, 3, 1, "equal"),
        ]

        styles = {
            "num":   {"bg": "#2d3561", "fg": "#e2e8f0", "active_bg": "#3d4571"},
            "op":    {"bg": "#e94560", "fg": "#ffffff", "active_bg": "#c73652"},
            "func":  {"bg": "#253555", "fg": "#a0b4d0", "active_bg": "#354565"},
            "clear": {"bg": "#e94560", "fg": "#ffffff", "active_bg": "#c73652"},
            "equal": {"bg": "#0f3460", "fg": "#ffffff", "active_bg": "#1a4a80"},
        }

        for (text, row, col, colspan, style) in buttons:
            s = styles[style]
            btn = tk.Button(
                btn_frame,
                text=text,
                bg=s["bg"],
                fg=s["fg"],
                activebackground=s["active_bg"],
                activeforeground=s["fg"],
                font=("Courier New", 20, "bold"),
                relief="flat",
                bd=0,
                cursor="hand2",
                command=lambda t=text: self._on_click(t),
            )
            btn.grid(
                row=row,
                column=col,
                columnspan=colspan,
                padx=5,
                pady=5,
                sticky="nsew",
            )

        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btn_frame.columnconfigure(j, weight=1)

        # Keyboard binding
        self.root.bind("<Key>", self._on_key)

    # ── Logic ──────────────────────────────────────────────────────────
    def _on_click(self, text):
        if text.isdigit() or text == ".":
            self._input_digit(text)
        elif text in ("÷", "×", "−", "+"):
            self._input_operator(text)
        elif text == "=":
            self._evaluate()
        elif text == "C":
            self._clear()
        elif text == "±":
            self._negate()
        elif text == "%":
            self._percent()

    def _on_key(self, event):
        key_map = {
            "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
            "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
            ".": ".", "/": "÷", "*": "×", "-": "−", "+": "+",
            "Return": "=", "KP_Enter": "=",
            "BackSpace": "C", "Escape": "C", "c": "C",
        }
        mapped = key_map.get(event.keysym) or key_map.get(event.char)
        if mapped:
            self._on_click(mapped)

    def _input_digit(self, d):
        current = self.display_var.get()
        if d == "." and "." in current and not self.new_number:
            return
        if self.new_number:
            self.display_var.set(d if d != "." else "0.")
            self.new_number = False
        else:
            if current == "0" and d != ".":
                self.display_var.set(d)
            else:
                self.display_var.set(current + d)

    def _input_operator(self, op):
        current = self.display_var.get()
        self.expression += current + op
        self.sub_display_var.set(self.expression)
        self.new_number = True

    def _evaluate(self):
        current = self.display_var.get()
        full_expr = self.expression + current
        self.sub_display_var.set(full_expr + " =")
        try:
            # Replace display symbols with Python operators
            py_expr = (
                full_expr
                .replace("÷", "/")
                .replace("×", "*")
                .replace("−", "-")
            )
            result = eval(py_expr)           # safe: only numeric input allowed
            result = self._fmt(result)
            self.display_var.set(result)
        except ZeroDivisionError:
            self.display_var.set("÷0 Error")
        except Exception:
            self.display_var.set("Error")
        self.expression = ""
        self.new_number = True

    def _clear(self):
        self.expression = ""
        self.display_var.set("0")
        self.sub_display_var.set("")
        self.new_number = True

    def _negate(self):
        val = self.display_var.get()
        try:
            num = float(val)
            self.display_var.set(self._fmt(-num))
        except ValueError:
            pass

    def _percent(self):
        val = self.display_var.get()
        try:
            num = float(val) / 100
            self.display_var.set(self._fmt(num))
        except ValueError:
            pass

    @staticmethod
    def _fmt(value):
        """Remove unnecessary trailing zeros."""
        if isinstance(value, float) and value == int(value):
            return str(int(value))
        return str(value)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
