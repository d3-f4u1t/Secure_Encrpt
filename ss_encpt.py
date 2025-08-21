import customtkinter as ctk
import os
from generate_rsa_keys import generate_keys
import tkinter.messagebox as msgbox
class ss_KeyGen():
    def __init__(self,root):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.frame = ctk.CTkFrame(root, fg_color = "#111111")
        self.frame.pack(fill="both", expand=True)


        root.config(bg = "#2b2b2b")
        self.title = ctk.CTkLabel(
            self.frame,
            text = "Key Generator",
            font = ctk.CTkFont(family="Segoe UI",size = 45, weight = "bold"),
            text_color = "white",
        )
        self.title.pack(pady= (100, 20))

        self.subtitle = ctk.CTkLabel(
            self.frame,
            text = "RSA",
            font = ctk.CTkFont(family="Segoe UI",size = 80, weight = "bold"),
            text_color = "white"
        )
        self.subtitle.pack(pady = (0, 100))

        self.gen_button = ctk.CTkButton(
            self.frame,
            text = "generate keys",
            font = ctk.CTkFont(size = 18),
            width = 200,
            height = 50,
            corner_radius = 12,
            command=self.run_keygen
             #to make this function go to the key generation function
        )
        
        self.gen_button.pack(pady = (0, 20))

    def run_keygen(self):
        generate_keys()
        msgbox.showinfo("Success", "RSA key pair generated and saved in /rsa_keys/")



    



    