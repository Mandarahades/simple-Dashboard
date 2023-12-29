import tkinter as tk
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def update_graph():
    # Fonction pour mettre à jour le graphique en fonction des données du tableau (non fourni dans cet exemple)
    # Ici, vous pouvez ajouter la logique pour mettre à jour les données du graphique en fonction du tableau
    pass


def generate_network_graph():
    G = nx.grid_2d_graph(5, 5)  # Exemple de génération d'un réseau maillé 5x5
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.title("Réseau maillé")
    plt.axis("off")
    plt.show()


def main():
    root = tk.Tk()
    root.title("Tableau de bord")

    # Bouton pour générer le réseau maillé
    network_button = tk.Button(root, text="Afficher Réseau Maillé", command=generate_network_graph)
    network_button.pack()

    # Graphique (exemple avec une figure statique)
    fig, ax = plt.subplots()
    ax.set_title('Graphique interactif')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    data = [1, 2, 3, 4, 5]
    ax.plot(data)
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Bouton pour mettre à jour le graphique
    update_button = tk.Button(root, text="Mettre à jour le graphique", command=update_graph)
    update_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
