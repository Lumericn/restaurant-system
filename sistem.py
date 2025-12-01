from models import Customer, Reservation, Menu, Order, DBReport
from function.lihat_menu import lihat_menu
from function.buat_reservasi import buat_reservasi
from function.buat_pesanan import buat_pesanan
from function.lihat_laporan import lihat_laporan
from function.hapus_pesanan import hapus_pesanan
from database import connect_db
import logging

logging.basicConfig(filename="debug.log", level=logging.ERROR)

while True:
    print("=== SISTEM RESTORAN ===")
    print("1. Lihat Menu")
    print("2. Buat Reservasi Meja")
    print("3. Buat Pesanan Menu")
    print("4. Lihat Laporan Reservasi & Pesanan")
    print("5. Hapus Pesanan")
    print("6. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        lihat_menu()
    elif pilihan == "2":
        buat_reservasi()
    elif pilihan == "3":
        buat_pesanan()
    elif pilihan == "4":
        lihat_laporan()
    elif pilihan == "5":
        hapus_pesanan()
    elif pilihan == "6":
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid!")
