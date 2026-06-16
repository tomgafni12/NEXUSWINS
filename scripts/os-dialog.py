#!/usr/bin/env python3
"""
Simple OS-like dialog using tkinter. Prints RESULT=<choice> to stdout.
"""
import sys
import os
try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import scrolledtext
except Exception:
    # We'll handle missing tkinter at runtime and fall back to console
    tk = None
    ttk = None
    scrolledtext = None


class OSDialog(tk.Tk):
    def __init__(self, title="NexusWins", message=None):
        super().__init__()
        self.title(title)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_cancel)
        self.result = None

        frm = ttk.Frame(self, padding=16)
        frm.grid()

        msg = message or "This is an operating-system style dialog.\nDo you want to continue?"
        lbl = ttk.Label(frm, text=msg, justify="left")
        lbl.grid(row=0, column=0, columnspan=3, sticky="w")

        btn_ok = ttk.Button(frm, text="OK", command=self.on_ok)
        btn_ok.grid(row=1, column=0, padx=(0,8), pady=(12,0))

        btn_cancel = ttk.Button(frm, text="Cancel", command=self.on_cancel)
        btn_cancel.grid(row=1, column=1, padx=(0,8), pady=(12,0))

        btn_details = ttk.Button(frm, text="Details", command=self.on_details)
        btn_details.grid(row=1, column=2, pady=(12,0))

        # Center window
        self.update_idletasks()
        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"+{x}+{y}")

    def on_ok(self):
        self.result = "OK"
        print("RESULT=OK")
        self.destroy()

    def on_cancel(self):
        self.result = "Cancel"
        print("RESULT=Cancel")
        self.destroy()

    def on_details(self):
        detail = tk.Toplevel(self)
        detail.title("Details")
        st = scrolledtext.ScrolledText(detail, width=60, height=15)
        st.pack(fill="both", expand=True, padx=8, pady=8)
        st.insert("1.0", "NexusWins OS-like dialog\n\nThis is a sample details window.\nYou can put diagnostic info, help text, or log output here.")
        st.config(state="disabled")


def main():
    # If no X display is available, fall back to a console prompt
    if not os.environ.get('DISPLAY') or tk is None:
        try:
            if sys.stdin.isatty():
                ans = input("This is an operating-system style dialog. Do you want to continue? [y/N]: ")
                if ans.strip().lower() in ('y', 'yes'):
                    print("RESULT=OK")
                    sys.exit(0)
                else:
                    print("RESULT=Cancel")
                    sys.exit(1)
            else:
                # Non-interactive environment: return Closed
                print("RESULT=Closed")
                sys.exit(1)
        except (EOFError, KeyboardInterrupt):
            print("RESULT=Closed")
            sys.exit(1)

    app = OSDialog()
    app.mainloop()
    if app.result is None:
        # window closed
        print("RESULT=Closed")
        sys.exit(1)
    sys.exit(0 if app.result == "OK" else 1)


if __name__ == "__main__":
    main()
