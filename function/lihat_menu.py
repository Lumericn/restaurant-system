from models import Customer, Reservation, Menu, Order, DBReport
from database import connect_db
import logging

def lihat_menu():
    try:
        # Koneksi ke database
        db = connect_db()
        if db is None:
            return  # Jika gagal koneksi, keluar dari fungsi

        cursor = db.cursor()

        # Ambil semua menu dari tabel menu_items
        cursor.execute("SELECT id, name, price FROM menu_items")
        menus = cursor.fetchall()  # Fetch semua hasil query

        # Tampilkan menu
        if not menus:
            print("Menu masih kosong!")  # Jika tidak ada data menu
        else:
            print("\n=== DAFTAR MENU ===")
            for m in menus:
                # m[0] = id, m[1] = name, m[2] = price
                print(f"{m[0]}. {m[1]} - Rp{m[2]}")

        # Tutup koneksi database
        db.close()

        input("\nTekan ENTER untuk kembali...")

    except Exception as e:
        # Tangani error dan catat log
        logging.error(f"Lihat Menu Error: {e}")
        print("Gagal menampilkan menu.")