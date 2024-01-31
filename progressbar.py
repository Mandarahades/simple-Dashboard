import tkinter as tk
from tkinter import ttk

class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trois Barres de Progression avec Canvas")
        self.root.geometry("600x200")

        # Créer un Canvas
        canvas = tk.Canvas(self.root)
        canvas.pack(expand=True, fill='both')

        # Créer les barres de progression avec Canvas
        self.create_progress_bars(canvas)

    def create_progress_bars(self, canvas):
        # 1
        progress_bar_1 = ttk.Progressbar(
            self.root, orient="horizontal", length=400, mode="determinate"
        )
        progress_bar_1["value"] = 30
        canvas.create_window(100, 50, window=progress_bar_1, anchor='nw')

        # 2
        progress_bar_2 = ttk.Progressbar(
            self.root, orient="horizontal", length=400, mode="determinate"
        )
        progress_bar_2["value"] = 50
        canvas.create_window(100, 100, window=progress_bar_2, anchor='nw')

        # 3
        progress_bar_3 = ttk.Progressbar(
            self.root, orient="horizontal", length=400, mode="determinate"
        )
        progress_bar_3["value"] = 75
        canvas.create_window(100, 150, window=progress_bar_3, anchor='nw')

        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressBarApp(root)
    root.mainloop()
