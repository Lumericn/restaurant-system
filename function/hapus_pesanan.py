from database import connect_db
import logging

def hapus_pesanan():
    """
    Menghapus pesanan menu dari database berdasarkan ID pesanan.
    """
    try:
        db = connect_db()
        if db is None:
            print("Koneksi database gagal!")
            return

        cursor = db.cursor()

        # Input ID pesanan yang akan dihapus
        order_id = input("Masukkan ID pesanan yang akan dihapus: ")

        # Cek apakah pesanan ada
        cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
        order = cursor.fetchone()
        if not order:
            print(f"Pesanan dengan ID {order_id} tidak ditemukan!")
            db.close()
            return

        # Hapus order_items terkait
        cursor.execute("DELETE FROM order_items WHERE order_id = %s", (order_id,))

        # Hapus order
        cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))

        db.commit()
        db.close()
        print("\n")
        print(f"Pesanan dengan ID {order_id} berhasil dihapus.")
        print("\n")

    except Exception as e:
        logging.error(f"Hapus Pesanan Error: {e}")
        print("Terjadi kesalahan saat menghapus pesanan.")
