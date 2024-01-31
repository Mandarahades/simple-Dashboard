import tkinter as tk
from tkinter import ttk
import data_1

class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ensemble de 3 barres de progression")
        self.root.geometry("400x150")

        # Lire les données du fichier data.py
        self.data_1 = data_1.data_1
        self.data_2 = data_1.data_2
        self.data_3 = data_1.data_3

        # Créer les barres de progression
        self.create_progress_bars()

    def create_progress_bars(self):
        style1 = ttk.Style()
        style1.configure("Color1.Horizontal.TProgressbar", troughcolor="lightgray", troughrelief="flat", thickness=30)

        style2 = ttk.Style()
        style2.configure("Color2.Horizontal.TProgressbar", troughcolor="lightgray", troughrelief="flat", thickness=30)

        style3 = ttk.Style()
        style3.configure("Color3.Horizontal.TProgressbar", troughcolor="lightgray", troughrelief="flat", thickness=30)

        # Barre de progression 1
        self.progress_bar_1 = ttk.Progressbar(
            self.root, orient="horizontal", length=300, mode="determinate",
            style="Color1.Horizontal.TProgressbar"
        )
        self.progress_bar_1["value"] = self.data_1["value"]
        self.progress_bar_1.grid(row=0, column=0, pady=20)
        self.progress_bar_1["maximum"] = 100
        self.set_progress_color(self.progress_bar_1, self.data_1["color"])

        # Barre de progression 2
        self.progress_bar_2 = ttk.Progressbar(
            self.root, orient="horizontal", length=300, mode="determinate",
            style="Color2.Horizontal.TProgressbar"
        )
        self.progress_bar_2["value"] = self.data_2["value"]
        self.progress_bar_2.grid(row=1, column=0, pady=20)
        self.progress_bar_2["maximum"] = 100
        self.set_progress_color(self.progress_bar_2, self.data_2["color"])

        # Barre de progression 3
        self.progress_bar_3 = ttk.Progressbar(
            self.root, orient="horizontal", length=300, mode="determinate",
            style="Color3.Horizontal.TProgressbar"
        )
        self.progress_bar_3["value"] = self.data_3["value"]
        self.progress_bar_3.grid(row=2, column=0, pady=20)
        self.progress_bar_3["maximum"] = 100
        self.set_progress_color(self.progress_bar_3, self.data_3["color"])

        # Bouton de fermeture de l'application
        close_button = tk.Button(
            self.root, text="Fermer", command=self.root.destroy
        )
        close_button.grid(row=3, column=0, pady=10)

def set_progress_color(self, progress_bar, color):
    progress_value = progress_bar["value"]
    normalized_value = progress_value / progress_bar["maximum"]
    red_component = int(255 * normalized_value)
    hex_color = "#{:02x}{:02x}{:02x}".format(red_component, 0, 0)
    style_name = progress_bar["style"].name
    progress_bar.style.map(style_name, foreground=[(normalized_value, color, hex_color)])


if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressBarApp(root)
    root.mainloop()
