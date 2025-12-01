from models import Customer, Reservation, DBReport
from database import connect_db
import logging

def buat_reservasi():
    try:
        print("\n=== BUAT RESERVASI ===")
        
        # Input data pelanggan
        name = input("Nama pelanggan: ")
        phone = input("Nomor HP: ")
        people = int(input("Jumlah orang: "))
        table_number = int(input("Nomor Meja: "))

        # Buat objek Customer dan Reservation
        customer = Customer(name, phone, people)
        reservation = Reservation(customer, table_number)

        # Koneksi ke database
        db = connect_db()
        if db is None:
            print("Koneksi database gagal!")
            return
        cursor = db.cursor()

        # Simpan data reservasi ke tabel reservations
        cursor.execute("""
            INSERT INTO reservations (customer_name, phone, people, table_number)
            VALUES (%s, %s, %s, %s)
        """, (customer.get_name(), customer.get_phone(), customer.get_people(), table_number))

        # Commit transaksi dan tutup koneksi
        db.commit()
        db.close()

        print("\nReservasi berhasil dibuat!")

    except Exception as e:
        # Tangani error dan catat di log
        logging.error(f"Reservation Error: {e}")
        print("Terjadi kesalahan saat menyimpan reservasi.")
