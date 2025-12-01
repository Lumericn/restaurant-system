import mysql.connector
import logging

logging.basicConfig(filename="debug.log", level=logging.ERROR)

def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",          # ganti jika ada password
            database="restoran"
        )
    except Exception as e:
        logging.error(f"Database Error: {e}")
        print("Gagal terhubung ke database!")
        return None