import customtkinter as ctk
from encryption import xor_encrypt, xor_decrypt, generate_random_key, binary_to_text


class EncryptionApp:
    def __init__(self, root):
        self.root = root
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        root.title("Secure Encryptor")
        root.geometry("800x600")

        self.frame = ctk.CTkFrame(root, fg_color="#111111")
        self.frame.pack(fill="both", expand=True)

        self.title = ctk.CTkLabel(
            self.frame,
            text="Encryption App",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color="white"
        )
        self.title.pack(pady=30)

        self.message_entry = ctk.CTkEntry(self.frame,placeholder_text= "Enter message", width = 600)
        self.message_entry.pack(pady=10)
        #key input
        self.key_entry = ctk.CTkEntry(self.frame,placeholder_text = "Enter key(optional)", width = 600)
        self.key_entry.pack(pady=10)

        #buttons for encrypt

        self.encrypt_button = ctk.CTkButton(
            self.frame,
            text = "Encrypt",
            command= self.encrypt_message,
        )
        self.encrypt_button.pack(pady= 10)

        self.decrypt_button = ctk.CTkButton(
            self.frame,
            text= "Decrypt",
            command = self.decrypt_message
        )
        self.decrypt_button.pack(pady = 10)

        #output box
        self.output_box = ctk.CTkTextbox(self.frame, width = 600, height = 200)
        self.output_box.pack(pady=10)

    def encrypt_message(self):
        message = self.message_entry.get()
        key = self.key_entry.get() or generate_random_key()#i have NOT added a way to input a key YET
        encrypted = xor_encrypt(message, key)
        self.output_box.delete("0.0","end")
        self.output_box.insert("0.0",f"Encrypted:\n{encrypted}\n\nKey:\n{key}")


    def decrypt_message(self):
        encrypted = self.message_entry.get()
        key = self.key_entry.get()

        if not key:
            self.output_box.delete("0.0", "end")
            self.output_box.insert("0.0", "Please provide a key for decryption.")
            return
                
        decrypted = xor_decrypt(encrypted, key)
        self.output_box.delete("0.0", "end")
        self.output_box.insert("0.0", f"Decrypted:\n{decrypted}")






        