 #this is for encrption/decryption logic
import random
import base64
import os
import shutil
from cryptography.hazmat.primitives import serialization #for importing keys and basic moving of keys(rsa,Xor)
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
#extra imports just for rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP



print("its working here")

def text_to_binary(text):
    """Convert text to binary string."""
    return ''.join(format(ord(c), '08b') for c in text)#c is character

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0,len(binary), 8)]
    return ''.join(chr(int(b, 2)) for b in chars)

def binary_to_base64(binary_str):
    byte_array = int(binary_str, 2).to_bytes(len(binary_str) // 8, byteorder='big')
    return base64.b64encode(byte_array).decode()  # Convert to Base64 string

# Convert Base64 back to binary string
def base64_to_binary(b64_str):
    byte_array = base64.b64decode(b64_str.encode())
    return ''.join(format(byte, '08b') for byte in byte_array)  # Convert back to binary


def generate_random_key(length=16):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(length))


#test


def xor_encrypt(plain_text,key):
    """Encrypt the plain text using XOR with the key."""
    binary_text = text_to_binary(plain_text)
    binary_key = text_to_binary(key)
    # Repeat the key to match the length of the plain text
    requested_key = (binary_key * (len(binary_text) // len(binary_key) + 1))[:len(binary_text)]

    # XOR operation
    encrypted_binary = ''.join('1' if binary_text[i] != requested_key[i] else '0' for i in range(len(binary_text)))                 

    return binary_to_base64(encrypted_binary)

    
def xor_decrypt(encrypted_base64, key):
    encrypted_binary = base64_to_binary(encrypted_base64)  # Convert Base64 back to binary
    binary_key = text_to_binary(key)
    requested_key = (binary_key * (len(encrypted_binary) // len(binary_key) + 1))[:len(encrypted_binary)]
    decrypted_binary = ''.join('1' if encrypted_binary[i] != requested_key[i] else '0' for i in range(len(encrypted_binary)))
    return binary_to_text(decrypted_binary)


def import_rsa_public_key(file_path, save_dir = "rsa_keys"):

    if not os.path.exists(save_dir): #cheks and makes sure file exists if note it'll create it
        os.makedirs(save_dir)

    filename = os.path.basename(file_path)
    save_path = os.path.join(save_dir, filename)

    with open(file_path,'rb') as f: #will read the key in binary format 'rb'
        public_key_data = f.read() #stored in this 


    #for key validation

    try:
        serialization.load_pem_public_key(public_key_data, backend=default_backend())
    except Exception as e:
        raise ValueError(f"Invalid public key file: {e}") from e
    
    with open(save_path, 'wb') as f:
        f.write(public_key_data)

    return save_path





def encrypt_xor_key_rsa(xor_key: bytes, public_key_path: str) -> bytes:
    #"""Encrypt the XOR key using RSA public key
    #returns the encrypted key as bytes

    #load public key again
    with open(public_key_path, 'rb') as f:
        public_key_path = f.read()

    try:
        public_key = serialization.load_pem_public_key(public_key_path, backend=default_backend())
    except Exception as e:
        raise ValueError(f"Invalid public key file: {e}") from e
    
    encrypted_key = public_key.encrypt(
        xor_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    def decrypt_xor_key_rsa(encrypted_key_b64: bytes, private_key_path: str) -> str:
        #decypt the rsa encrypted xor key usingthe privite key
        with open(private_key_path, "rb") as f:
            private_key = RSA.import_key(f.read())

        cipher_rsa = PKCS1_OAEP.new(private_key)

        encrypted_key = base64.b64decode(encrypted_key_b64)
        decrypted_key = cipher_rsa.decrypt(encrypted_key)
        return decrypted_key.decode()  # Convert bytes back to string



    return encrypted_key



