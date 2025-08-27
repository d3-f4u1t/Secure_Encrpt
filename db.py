import mysql.connector
from dotenv import load_dotenv
import os
#loading the file from a specific location
load_dotenv(r"C:\Users\hkpan\.ENV FILES/.env")

def get_connection():
    return mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        database = os.getenv("DB_NAME")

    )

def save_encryption(message, xor_key, rsa_encrypted_key):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO encrypted_data (message, xor_key, rsa_encrypted_key) VALUES (%s, %s, %s)",
        (message, xor_key, rsa_encrypted_key)


    )
    conn.commit()
    cursor.close()
    conn.close()
