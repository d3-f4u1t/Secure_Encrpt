import mysql.connector
from dotenv import load_dotenv
import os
#loading the file from a specific location
load_dotenv(r"C:\Users\hkpan\.ENV FILES/.env")

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

def get_server_connection():
    return mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASS
    )

def get_db_connection():
    return mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASS,
        database = DB_NAME
    )

#create database if not alaready exists

def create_database():
    conn = get_server_connection()
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.close()


# to create table if not already exists

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS encrypted_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        meaaage TEXT NOT NULL,
        xor_key TEXT NOT NULL,
        rsa_encryted_key TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()




def save_encryption(message, xor_key, rsa_encrypted_key):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO encrypted_data (message, xor_key, rsa_encrypted_key) VALUES (%s, %s, %s)",
        (message, xor_key, rsa_encrypted_key)


    )
    conn.commit()
    cursor.close()
    conn.close()
