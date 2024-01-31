import tkinter as tk
from tkinter import ttk

class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Barre de Progression Multicolore")
        self.root.geometry("600x200")

        # Créer une Progressbar
        self.progress_bar = ttk.Progressbar(
            self.root, orient="horizontal", length=400, mode="determinate"
        )
        self.progress_bar["value"] = 50
        self.progress_bar.pack(pady=20)

        # Bouton de fermeture de l'application
        close_button = tk.Button(
            self.root, text="Fermer", command=self.root.destroy
        )
        close_button.pack(pady=10)

        # Définir les couleurs de la Progressbar
        self.set_progress_color()

    def set_progress_color(self):
        progress_value = self.progress_bar["value"]
        normalized_value = progress_value / self.progress_bar["maximum"]

        # Définir les couleurs pour chaque segment de la Progressbar
        color1 = "#FF0000"  # Rouge
        color2 = "#FFFF00"  # Jaune
        color3 = "#00FF00"  # Vert

        # Calculer les positions de séparation des segments
        segment1_end = normalized_value / 3
        segment2_end = 2 * normalized_value / 3

        # Configurer le style pour chaque segment
        self.progress_bar.style = ttk.Style()
        self.progress_bar.style.configure("Color1.Horizontal.TProgressbar", troughcolor="lightgray", troughrelief="flat", thickness=30, background=color1)
        self.progress_bar.style.map("Color1.Horizontal.TProgressbar", field=[("troughcolor", color1)])

        self.progress_bar.style.configure("Color2.Horizontal.TProgressbar", troughcolor="lightgray", troughrelief="flat", thickness=30, background=color2)
        self.progress_bar.style.map("Color2.Horizontal.TProgressbar", field=[("troughcolor", color2)])

        self.progress_bar.style.configure("Color3.Horizontal.TProgressbar", troughcolor="lightgray", troughrelief="flat", thickness=30, background=color3)
        self.progress_bar.style.map("Color3.Horizontal.TProgressbar", field=[("troughcolor", color3)])

        # Configurer la Progressbar avec les segments de couleur
        self.progress_bar["style"] = "Color1.Horizontal.TProgressbar"
        self.progress_bar["maximum"] = 1.0

        self.progress_bar.selection_set(0, segment1_end)
        self.progress_bar.selection_set(segment1_end, segment2_end)
        self.progress_bar.selection_set(segment2_end, 1.0)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressBarApp(root)
    root.mainloop()
