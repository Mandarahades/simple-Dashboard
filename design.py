import tkinter as tk

# -------------------------- DEFINING GLOBAL VARIABLES -------------------------
# these are just the colors we'll be using to paint our rooms (frames)
selectionbar_color = '#eff5f6'
sidebar_color = '#F5E1FD'
header_color = '#53366b'
visualisation_frame_color = "#ffffff"

# ------------------------------- ROOT WINDOW ----------------------------------


class TkinterApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Attendance Tracking App")

        # ------------- BASIC APP LAYOUT -----------------

        self.geometry("1100x700")
        self.resizable(0, 0)
        self.title('Attendance Tracking System')
        self.config(background=selectionbar_color)
        icon = tk.PhotoImage(file='logo.png')
        self.iconphoto(True, icon)

        # ---------------- HEADER ------------------------

        self.header = tk.Frame(self, bg=header_color)
        self.header.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.1)

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
        
        #----------------------- SUBMENU------------------------------
        #        TO BE ADDED IN THE SECTION 5 OF ARTICLE  
        #             5.Integrating Everything together
        #-------------------------------------------------------------

        # --------------------  MAIN FRAME ---------------------------

        main_frame = tk.Frame(self)
        main_frame.place(relx=0.3, rely=0.1, relwidth=0.7, relheight=0.9)

        # ------------------ MULTI PAGE SETTINGS ----------------------
        #        TO BE ADDED IN THE SECTION 3 OF ARTICLE 
        #                   3.Multipage settings
        #--------------------------------------------------------------


app = TkinterApp()
app.mainloop()