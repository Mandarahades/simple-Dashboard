import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data
from PIL import Image, ImageTk

plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#4C2A85", "#BE96FF", "#9557DADA", "#9E366E", "#A98CCC"])

# chart 1: Bar chart of sales data
fig1, ax1 = plt.subplots()



ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Classification trafic")
ax1.set_xlabel("Product")
ax1.set_ylabel("Sales")
#plt.show()

# chart 2: Horizontal bar
fig2, ax2 = plt.subplots()
ax2.barh( list(inventory_data.keys()), inventory_data.values())
ax2.set_title(" classification représentation 2")
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
plt.show()

# Creation de la fenêtre 
root = tk.Tk()
root.title("Projet reseaux")
root.state('zoomed')

side_frame = tk.Frame(root, bg="#4C2A85")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text='Dashboard', bg="#4C2A85", fg="#fff", font=25)
label.pack(pady=50, padx=40)

charts_frame = tk.Frame(root)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)
canvas1 = FigureCanvasTkAgg(fig3, upper_frame)
image_path="prot2.jpg"
img = Image.open(image_path)
photo = ImageTk.PhotoImage(img)


canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig1, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side='left', fill='both', expand=True)

canvas2.create_image(0, 0, anchor=tk.NW, image=photo)

lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill='both', expand=True)


canvas3 = FigureCanvasTkAgg(fig2, lower_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side='left', fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig5, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side='left', fill="both", expand=True)


root.mainloop()

