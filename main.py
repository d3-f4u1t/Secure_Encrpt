import customtkinter as ctk
from splash_screen import SplashScreen
from encryption_app import EncryptionApp


def show_main_app():
    splash_root.destroy()
    main_root = ctk.CTk()
    app = EncryptionApp(main_root)
    main_root.mainloop()

splash_root = ctk.CTk()
SplashScreen(splash_root, on_enter_callback=show_main_app)
splash_root.mainloop()
