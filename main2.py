import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sidebar_color = '#F5E1FD'
header_color = '#53366b'


from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data

plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#4C2A85", "#BE96FF", "#9557DADA", "#9E366E", "#A98CCC"])

# chart 1: Bar chart of sales data
fig1, ax1 = plt.subplots()


ax1.clear()
ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Classification trafic")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")
#plt.show()

# chart 2: Horizontal bar
fig2, ax2 = plt.subplots()
ax2.clear()
ax2.barh( list(inventory_data.keys()), inventory_data.values())
ax2.set_title(" Consomation des Noeuds")
ax2.set_xlabel("Product")
ax2.set_ylabel("Sales")
#plt.show()

# chart 3: Pie  chart of product data
fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
ax3.set_title(" pourcentage représentation")
#plt.show()

# chart 4: line chart of sales by year

fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title(" ensemble de graphe ")
ax4.set_xlabel("intervale de temps")
ax4.set_ylabel("Trafic")
#plt.show()

# chart 5: Area chart 
fig5, ax5 = plt.subplots()
ax5.fill_between(inventory_month_data.keys(), inventory_month_data.values())
ax5.set_xlabel("INTERVAL")
ax5.set_ylabel("Trafic")


# Creation de la fenêtre 
root = tk.Tk()
root.title("Monitoning Reseaux")
root.state('zoomed')

side_frame = tk.Frame(root, bg="#4C2A85")
side_frame.pack(side="left", fill="y")
def __init__(self):
# ---------------- SIDEBAR -----------------------
                # SIDEBAR FRAME
        self.sidebar = tk.Frame(self, bg=sidebar_color)
        self.sidebar.place(relx=0, rely=0, relwidth=0.3, relheight=1)

                # BRANDING FRAME (UNIVERSITY LOGO AND NAME)
        self.brand_frame = tk.Frame(self.sidebar, bg=sidebar_color)
        self.brand_frame.place(relx=0, rely=0, relwidth=1, relheight=0.15)
        self.uni_logo = icon.subsample(9)
        logo = tk.Label(self.brand_frame, image=self.uni_logo, bg=sidebar_color)
        logo.place(x=5, y=20)

        uni_name = tk.Label(self.brand_frame,
                                    text='ABC',
                                    bg=sidebar_color,
                                    font=("", 15, "bold")
                                    )
        uni_name.place(x=55, y=27, anchor="w")

        uni_name = tk.Label(self.brand_frame,
                                    text='University',
                                    bg=sidebar_color,
                                    font=("", 15, "bold")
                                    )
        uni_name.place(x=55, y=60, anchor="w")
                
                # SUBMENU FRAME (FOR PLACING SUBMENUS)
        self.submenu_frame = tk.Frame(self.sidebar, bg=sidebar_color)
        self.submenu_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.85)

label = tk.Label(side_frame, text='Dashboard', bg="#4C2A85", fg="#fff", font=25)
label.pack(pady=50, padx=40)

# refresh button
def refresh():
    # refresh the charts
    pass
btn = tk.Button(side_frame, text="Refresh", command=refresh, bg="#4C2A85", fg="#fff", font=25)
btn.pack(pady=400, padx=80)


charts_frame = tk.Frame(root)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)


# Création de l'image à intégrer dans le Canvas
image_path = "prot2.png"  # Remplacez ceci par le chemin de votre image
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)


# Affichage de l'image à l'intérieur du Canvas
canvas_img = tk.Canvas(upper_frame, width=700, height=500)
canvas_img.create_image(0, 0, anchor=tk.NW, image=photo)
canvas_img.pack(side="left") 

canvas2 = FigureCanvasTkAgg(fig1, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side='left', fill='both', expand=True)

lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill='both', expand=True)


canvas3 = FigureCanvasTkAgg(fig2, lower_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side='left', fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig5, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side='left', fill="both", expand=True)







root.mainloop()
