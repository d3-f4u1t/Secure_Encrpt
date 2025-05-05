import customtkinter as ctk
import webbrowser

#just for the ss 
#main start is at main.py
class SplashScreen:
    def __init__(self, root, on_enter_callback):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        
        root.configure(bg = "#1E1E1E")

        self.frame = ctk.CTkFrame(root, fg_color = "#111111")
        self.frame.pack(expand = True, fill = "both")

        self.title = ctk.CTkLabel(
            self.frame,
            text = "SECURE ENCRPT",
            font = ctk.CTkFont(family="Segoe UI",size = 80, weight = "bold"),
            text_color = "white"

        )

        self.title.pack(pady = (100, 20))


        self.credits = ctk.CTkLabel(
            self.frame,
            text = "Made by D3FAU1T",
            font = ctk.CTkFont(size = 24, weight= "normal"),
            text_color = "gray"
        )

        self.credits.pack(pady = (0, 60))


        # Subtitle / tagline
        self.subtitle = ctk.CTkLabel(
           self.frame,
           text="Encrypt and Decrypt any phrase with Ease",
           font=ctk.CTkFont(size=45, weight="bold", slant="italic"),  # slanted for style
           text_color="white"
        )


        self.subtitle.pack(pady=(0, 100))

        self.subtitle = ctk.CTkLabel(
           self.frame,
           text="This is as easy as it gets\n take any phrase and encrypt it\n not just that but also decrypt it",
           font=ctk.CTkFont(size=45, weight="normal", family="Courier"),  #slanted for style
           text_color="gray"
        )
        self.subtitle.pack(pady=(0, 110))


        self.enter_button = ctk.CTkButton(
            self.frame,
            text = "Enter",
            font = ctk.CTkFont(size = 18),
            width = 200,
            height = 50,
            corner_radius = 12,
            command = on_enter_callback
        )

        self.enter_button.pack(pady= 50, side = "bottom")

#


        self.sidebar_width = 300
        self.sidebar_open = False


        self.sidebar = ctk.CTkFrame(
            root,
            width= self.sidebar_width,
            fg_color= "#333333",
            corner_radius= 0

        )
        self.sidebar.place(x=- self.sidebar_width, y=0, relheight = 1.0)
        self.update_sidebar_height(root)


        #root.bind("<Configure>", self.on_resize)

        
        


        self.sidebar_top_band = ctk.CTkFrame(
           self.sidebar,
           height=50,
           fg_color="#222222",
           corner_radius=0
        )
        self.sidebar_top_band.pack(side="top", fill="x")


        self.toggle_button = ctk.CTkButton(
            root,
            text = "☰",
            font = ctk.CTkFont(size = 20),
            width = 35,
            height = 35,
            corner_radius = 12,
            command = self.toggle_sidebar
        )
        self.toggle_button.place(x = 10, y = 10)
        self.toggle_button.lift()

        self.root = root
        self.root.after(100, lambda: self.root.attributes("-fullscreen", True))

        

        self.minimize_button = ctk.CTkButton(
            root,
            text="-",
            font = ctk.CTkFont(size = 16),
            width=35,
            height=35,
            corner_radius=12,
            command= self.minimize
        )

        


        self.close_button = ctk.CTkButton(
            root,
            text="X",
            font = ctk.CTkFont(size = 16),
            width=35,
            height=35,
            corner_radius=12,
            fg_color="red",
            command= root.quit
        )

        self.root.after(200, self.place_top_right_buttons)

        self.discord_button = ctk.CTkButton(
            self.sidebar,
            text ="My Discord",
            font = ctk.CTkFont(size = 16),
            width = 150,
            height = 35,
            corner_radius = 12,
            command= self.open_discord
        
        )
        self.discord_button.pack(pady=10)






        #main content frame

        

        
    def toggle_sidebar(self):
        if not self.sidebar_open:
             #to remove the sliderbar from the screen
            self.sidebar.place(x=0, y=0, relheight = 1.0)
            
            self.sidebar.lift()
            self.toggle_button.lift()
            self.sidebar_open = True

        else:
            
            self.sidebar.place(x= - self.sidebar_width, y=0, relheight = 1.0)
            
            self.toggle_button.lift()
            self.sidebar_open = False

    def on_resize(self, event):
        self.update_sidebar_height(event.widget)
        self.place_top_right_buttons()

    def update_sidebar_height(self, root):
        height = root.winfo_height()
        self.sidebar.place_configure(height=height)
# Minimizes the window
    def minimize(self):
        self.root.iconify()

    def place_top_right_buttons(self):
            width = self.root.winfo_width()
            spacing = 10
            self.close_button.place(x=width - 45, y=10)
            self.minimize_button.place(x=width - 90, y=10)

    def open_discord(self):
        webbrowser.open_new("http://discordapp.com/users/873571615852617760") 


    #stuff inside the sidebar

    


        




