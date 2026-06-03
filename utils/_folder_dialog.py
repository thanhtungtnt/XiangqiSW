"""Standalone script launched as a subprocess to open a Tk folder dialog."""

import sys
import os
import tkinter as tk
from tkinter import filedialog

def main() -> None:
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    try:
        # Mở hộp thoại chỉ cho phép chọn thư mục
        folder_path = filedialog.askdirectory(
            title="Chọn thư mục chứa ảnh cờ / Select folder"
        )
    finally:
        root.destroy()

    # In ra đường dẫn thư mục để file cha (app.py) có thể đọc được
    sys.stdout.write(folder_path or "")

if __name__ == "__main__":
    main()