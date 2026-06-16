#!/usr/bin/env python3
"""
Primitive OS-style modal dialog (tkinter)
Exits with code 0 for 'Continue', 1 for 'Cancel', 2 for timeout
"""
import sys
import tkinter as tk
from tkinter import font

def run_modal(title, message, timeout=None):
    root = tk.Tk()
    root.withdraw()

    # Create a top-level window to style like a primitive OS
    win = tk.Toplevel(root)
    win.title(title)
    win.resizable(False, False)

    # Retro colors and font
    bg = "#c0c0c0"
    fg = "#000000"
    accent = "#008080"

    win.configure(bg=bg)

    # Center window
    w, h = 420, 160
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws - w) // 2
    y = (hs - h) // 2
    win.geometry(f"{w}x{h}+{x}+{y}")

    # Make window modal
    win.transient(root)
    win.grab_set()

    # Title bar (custom look)
    title_frame = tk.Frame(win, bg=accent, height=28)
    title_frame.pack(fill=tk.X, side=tk.TOP)
    tfont = font.Font(family="Helvetica", size=10, weight="bold")
    tk.Label(title_frame, text=title, bg=accent, fg="white", font=tfont).pack(padx=8, pady=4, anchor="w")

    # Message area
    body = tk.Frame(win, bg=bg)
    body.pack(expand=True, fill=tk.BOTH, padx=12, pady=12)
    mfont = font.Font(family="Courier", size=11)
    tk.Label(body, text=message, bg=bg, fg=fg, font=mfont, justify="left", wraplength=380).pack(anchor="w")

    result = {"code": None}

    def on_continue():
        result["code"] = 0
        win.destroy()

    def on_cancel():
        result["code"] = 1
        win.destroy()

    # Buttons
    btn_frame = tk.Frame(win, bg=bg)
    btn_frame.pack(fill=tk.X, padx=12, pady=(0,12))
    cbtn = tk.Button(btn_frame, text="Continue", width=12, command=on_continue)
    cbtn.pack(side=tk.RIGHT, padx=6)
    bbtn = tk.Button(btn_frame, text="Cancel", width=12, command=on_cancel)
    bbtn.pack(side=tk.RIGHT)

    # Keyboard bindings
    win.bind('<Return>', lambda e: on_continue())
    win.bind('<Escape>', lambda e: on_cancel())

    # Optional timeout
    if timeout is not None:
        def do_timeout():
            if result["code"] is None:
                result["code"] = 2
                try:
                    win.destroy()
                except Exception:
                    pass
        win.after(int(timeout * 1000), do_timeout)

    # Start loop
    root.deiconify()
    root.wait_window(win)
    root.destroy()
    return result["code"]

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--title', default='NexusWins', help='Dialog title')
    p.add_argument('--message', default='This is a primitive OS-style modal.', help='Dialog message')
    p.add_argument('--timeout', type=float, default=None, help='Seconds before auto-cancel')
    args = p.parse_args()

    try:
        code = run_modal(args.title, args.message, args.timeout)
    except tk.TclError as e:
        # No display available
        print(args.message)
        ans = input('Continue? [y/N]: ').strip().lower()
        code = 0 if ans == 'y' else 1

    sys.exit(code if code is not None else 1)

if __name__ == '__main__':
    main()
