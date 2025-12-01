from models import Customer, Reservation, Menu, Order, DBReport
from function.lihat_menu import lihat_menu
from function.buat_reservasi import buat_reservasi
from function.buat_pesanan import buat_pesanan
from function.lihat_laporan import lihat_laporan
from database import connect_db
import logging

logging.basicConfig(filename="debug.log", level=logging.ERROR)

while True:
    print("\n=== SISTEM RESTORAN ===")
    print("1. Lihat Menu")
    print("2. Buat Reservasi Meja")
    print("3. Buat Pesanan Menu")
    print("4. Lihat Laporan Reservasi")
    print("5. Keluar")

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
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")