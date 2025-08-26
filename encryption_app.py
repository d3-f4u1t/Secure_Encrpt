import customtkinter as ctk
from encryption import xor_encrypt, xor_decrypt, generate_random_key, binary_to_text
from tkinter import messagebox, filedialog
from encryption import import_rsa_public_key #same as there
from encryption import encrypt_xor_key_rsa
import base64
import os
from ss_encpt import ss_KeyGen
import tkinter as tk







class EncryptionApp:
    def __init__(self, root):
        self.root = root
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.import_true = False
        self.encrypt_xor_button = None

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
        self.key_efromntry = ctk.CTkEntry(self.frame,placeholder_text = "Enter key(it's recommended to keep the length of the key same as the phrase and the letters u unique)", width = 600)
        self.key_entry = ctk.CTkEntry(self.frame, placeholder_text="Enter XOR Key", width=600)
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

        self.import_key_button = ctk.CTkButton(
            self.frame,
            text = "Import Public Key",
            command= self.select_public_key_file,

        )
        self.import_key_button.pack(pady=10)

        self.keygen_window_button = ctk.CTkButton(
            self.frame,
            text = "Generate RSA Keys",
            command = self.open_keygen_window

        )

        self.keygen_window_button.pack(pady=10)

        self.output_box = ctk.CTkTextbox(self.frame, width = 600, height = 200)
        self.output_box.pack(pady=10)

        self.decrypt_xor_button = ctk.CTkButton(
            self.frame,
            text = "Decrypt XOR Key with RSA",
            command = self.decrypt_xor_key_rsa
        )
        self.decrypt_xor_button.pack(pady = 10)

        
    def open_keygen_window(self):
        keygen_window = tk.Toplevel(self.root)
        keygen_window.title("RSA KEY GENERATOR")
        keygen_window.geometry("800x600")
        ss_KeyGen(keygen_window)


        

        

        #output box
        

    # Check for any .pem file in rsa_keys folder
        pem_files = [f for f in os.listdir("rsa_keys") if f.endswith(".pem")]
        if pem_files:
            self.public_key_filename = pem_files[0]  # use the first .pem file found
            self.import_true = True
            self.create_encrypt_xor_button()
#same as the other part below but this one is for already existing keys
    def create_encrypt_xor_button(self):
        if self.encrypt_xor_button is None:
            self.encrypt_xor_button = ctk.CTkButton(
                self.frame,
                text="Encrypt XOR Key with RSA",
                command=self.encrypt_xor_key_rsa
            )
            self.encrypt_xor_button.pack(pady=10)

    

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



    def select_public_key_file(self):
        file_path = filedialog.askopenfilename(
            title = "select public key file",
            filetypes= [("PEM files", "*.pem")]
        )
        if file_path:
            try:

                # Extract and store just the filename (not full path)
                self.public_key_filename = os.path.basename(file_path)
                import_rsa_public_key(file_path)
                messagebox.showinfo("Success", "Public key imported successfully.")
                self.import_true = True

                if self.encrypt_xor_button is None:
                    self.encrypt_xor_button = ctk.CTkButton(
                        self.frame,
                        text = "Encrypt XOR Key with RSA",
                        command = self.encrypt_xor_key_rsa
                    )
                    self.encrypt_xor_button.pack(pady=10)
                self.auto_encrypt_xor_key()

            except Exception as e:
                messagebox.showerror("Error", f"Failed to import public key:\n {e}")
                self.import_true = False

    def encrypt_xor_key_rsa(self):
          # Optional: re-import here if needed

        key = self.key_entry.get()
        xor_key_bytes = key.encode()
        pub_key_path = os.path.join("rsa_keys", self.public_key_filename)

        if not key:
            messagebox.showerror("Error", "Please enter a XOR key to encrypt.")
            return

            xor_key_bytes = key.encode()
            pub_key_path = "rsa_keys/public_key.pem"  # Adjust if your key has a different name or path

        try:
            encrypted_key = encrypt_xor_key_rsa(xor_key_bytes, pub_key_path)
            encoded_key = base64.b64encode(encrypted_key).decode()
            self.output_box.delete("0.0", "end")
            self.output_box.insert("0.0", f"Encrypted XOR Key with RSA:\n{encoded_key}")
        except Exception as e:
            messagebox.showerror("Error", f"RSA encryption failed:\n{e}")

    def auto_encrypt_xor_key(self):
        key = self.key_entry.get()

        if not key:
            messagebox.showinfo("Missing XOR key, please emter a xor key first to encrypt.")
            return
        
        try:
            xor_key_bytes = key.encode()
            pub_key_path = os.path.join("rsa_keys", self.public_key_filename)

            encrypted_key = encrypt_xor_key_rsa(xor_key_bytes, pub_key_path)
            encoded_key = base64.b64encode(encrypted_key).decode()
            self.output_box.delete("0.0", "end")
            self.output_box.insert("0.0", f"Encrypted XOR Key with RSA:\n{encoded_key}")  
        except Exception as e:
            messagebox.showerror("Error", f"RSA encryption failed:\n{e}")

    def decrypt_xor_key_rsa(self):
        encrypted_key_b64 = self.message_entry.get()
        priv_key_path = filedialog.askopenfilename(
            title = "Select Private Key File",
            filetypes = [("PEN files",".pem")]

        )

        if not priv_key_path:
            return
        
        try:
            from encryption import decrypt_xor_key
            xor_key = decrypt_xor_key(encrypted_key_b64, priv_key_path)

            self.output_box.delete("0.0", "end")
            self.output_box.insert("0.0", f"Decrypted XOR Key:\n{xor_key}")

        except Exception as e:
            messagebox.showerror("Error", f"RSA decryption failed:\n{e}")
            






        


        