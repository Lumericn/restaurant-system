from models import Customer, Menu, Order
from database import connect_db

def buat_pesanan():
    try:
        print("\n=== PEMBUATAN PESANAN MENU ===")
        
        # Input data pelanggan
        name = input("Nama pelanggan: ")
        phone = input("Nomor HP: ")
        people = int(input("Jumlah orang: "))
        table_number = int(input("Nomor Meja: "))

        # Buat objek Customer
        customer = Customer(name, phone, people)

        # Koneksi ke database
        db = connect_db()
        if db is None:
            print("Koneksi database gagal!")
            return
        cursor = db.cursor()

        # Ambil daftar menu dari database
        cursor.execute("SELECT id, name, price FROM menu_items")
        menus = cursor.fetchall()

        if not menus:
            print("Menu masih kosong!")
            return

        # Tampilkan menu ke pengguna
        print("\n=== DAFTAR MENU ===")
        for m in menus:
            print(f"{m[0]}. {m[1]} - Rp{m[2]}")

        # Input menu yang dipesan (dalam format ID, pisahkan dengan koma)
        pilihan = input("\nMasukkan ID menu (pisahkan dengan koma, contoh: 1,3,4): ")
        pilihan_ids = [int(x.strip()) for x in pilihan.split(",")]

        # Buat daftar objek Menu sesuai pilihan
        ordered_items = [Menu(m[0], m[1], m[2]) for m in menus if m[0] in pilihan_ids]
        if not ordered_items:
            print("Menu tidak valid!")
            return

        # 7. Buat objek Order dengan informasi pelanggan, menu yang dipilih, dan nomor meja
        order = Order(customer, ordered_items, table_number)

        # Hitung total harga pesanan
        total_price = sum(item.price for item in ordered_items)

        # Simpan data order ke tabel orders
        cursor.execute("""
            INSERT INTO orders (customer_name, phone, table_number, total_price)
            VALUES (%s, %s, %s, %s)
        """, (customer.get_name(), customer.get_phone(), table_number, total_price))
        order_id = cursor.lastrowid  # Ambil ID order terakhir yang dibuat

        # Simpan setiap item pesanan ke tabel order_items
        for m in ordered_items:
            cursor.execute("""
                INSERT INTO order_items (order_id, menu_id, quantity, price)
                VALUES (%s, %s, %s, %s)
            """, (order_id, m.menu_id, 1, m.price))

        # Commit transaksi dan tutup koneksi database
        db.commit()
        db.close()

        # Cetak struk pesanan ke layar
        print("\n=== STRUK PEMBELIAN ===")
        order.print_receipt()
        print("\nPesanan selesai!")

    except Exception as e:
        # Menangkap semua error, tampilkan pesan dan traceback untuk debugging
        import traceback
        print("Terjadi kesalahan saat membuat pesanan:", e)
        traceback.print_exc()
