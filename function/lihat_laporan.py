from models import Customer, Reservation, Menu, Order, DBReport
from database import connect_db
import logging

def lihat_laporan():
    try:
        # Koneksi ke database
        db = connect_db()
        if db is None:
            print("Koneksi database gagal!")
            return
        cursor = db.cursor()

        # Tampilkan laporan reservasi
        print("\n=== LAPORAN RESERVASI MEJA ===")
        cursor.execute("SELECT * FROM reservations")  # Ambil semua data dari tabel reservations
        reservations = cursor.fetchall()  # Fetch semua hasil query
        for r in reservations:
            print(r)  # Cetak tiap reservasi

        # Tampilkan laporan pemesanan menu
        print("\n=== LAPORAN PEMESANAN MENU ===")
        # Mengambil data pesanan dengan join antar tabel: orders, order_items, menu_items
        cursor.execute("""
            SELECT o.id, o.customer_name, o.phone, o.table_number,
                   m.name, oi.quantity, oi.price, o.total_price, o.order_time
            FROM orders o
            JOIN order_items oi ON o.id = oi.order_id
            JOIN menu_items m ON oi.menu_id = m.id
        """)
        orders = cursor.fetchall()  # Fetch semua hasil query
        if not orders:
            print("Belum ada pesanan.")  # Jika tidak ada data
        else:
            for o in orders:
                print(o)  # Cetak tiap detail pesanan

        # Tutup koneksi database
        db.close()

    except Exception as e:
        # Tangani error dan tampilkan traceback agar lebih mudah debug
        import traceback
        print("Terjadi kesalahan saat mengambil laporan:", e)
        traceback.print_exc()
    
    print ("\n")