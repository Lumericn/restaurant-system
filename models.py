from typing import List

# =================================================
# Kelas Customer
# =================================================
class Customer:
    """
    Menyimpan informasi pelanggan.
    Attributes:
        name (str): Nama pelanggan.
        phone (str): Nomor HP pelanggan.
        people (int): Jumlah orang untuk reservasi.
    """
    def __init__(self, name: str, phone: str, people: int):
        self.__name = name
        self.__phone = phone
        self.__people = people

    # Getter
    def get_name(self) -> str:
        return self.__name

    def get_phone(self) -> str:
        return self.__phone

    def get_people(self) -> int:
        return self.__people

    # Setter
    def set_phone(self, new_phone: str):
        self.__phone = new_phone

# =================================================
# Kelas Menu
# =================================================
class Menu:
    """
    Menyimpan data menu makanan/minuman.

    Attributes:
        menu_id (int): ID menu.
        name (str): Nama menu.
        price (int): Harga menu.
    """
    def __init__(self, menu_id: int, name: str, price: int):
        self.menu_id = menu_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.menu_id}. {self.name} - Rp{self.price}"

# =================================================
# Base class Entity
# =================================================
class Entity:
    """Kelas dasar untuk entitas yang berhubungan dengan Customer."""
    def __init__(self, customer: Customer):
        self.customer = customer

# =================================================
# Kelas Reservation
# =================================================
class Reservation(Entity):
    """
    Menyimpan informasi reservasi meja.

    Attributes:
        customer (Customer): Objek pelanggan.
        table_number (int): Nomor meja yang dipesan.
    """
    def __init__(self, customer: Customer, table_number: int):
        super().__init__(customer)
        self.table_number = table_number

# =================================================
# Kelas Order
# =================================================
class Order(Entity):
    """
    Menyimpan daftar pesanan menu.

    Attributes:
        customer (Customer): Objek pelanggan.
        items (List[Menu]): Daftar menu yang dipesan.
        table_number (int): Nomor meja.
    """
    def __init__(self, customer: Customer, items: List[Menu], table_number: int):
        super().__init__(customer)
        self.items = items
        self.table_number = table_number

    def total_price(self) -> int:
        """Menghitung total harga semua menu yang dipesan."""
        return sum(item.price for item in self.items)

    def print_receipt(self):
        """Menampilkan struk pembayaran ke layar."""
        print("\n===== STRUK PEMBAYARAN =====")
        print(f"Nama: {self.customer.get_name()}")
        print(f"No HP: {self.customer.get_phone()}")
        print(f"Jumlah Orang: {self.customer.get_people()}")
        print(f"Nomor Meja: {self.table_number}")
        print("---------------------------")
        for item in self.items:
            print(f"{item.name} - Rp{item.price}")
        print("---------------------------")
        print(f"TOTAL: Rp{self.total_price()}")
        print("============================")

# =================================================
# POLYMORPHISM: Report
# =================================================
class Report:
    """Kelas dasar untuk laporan."""
    def print(self):
        raise NotImplementedError

class TextReport(Report):
    """Laporan berbasis teks sederhana."""
    def print(self):
        print("[Laporan Teks] Menampilkan laporan sederhana...")

class DBReport(Report):
    """Laporan berbasis database."""
    def print(self):
        print("[Laporan Database] Membaca laporan dari database...")
        
        
#docstring web/html: py -m pydoc -w models
#docstring : py -m pydoc models