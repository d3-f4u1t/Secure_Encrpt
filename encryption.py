#this is for encrption/decryption logic
import random
import base64
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

