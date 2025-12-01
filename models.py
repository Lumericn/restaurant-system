from typing import List

# =================================================
# Kelas Customer
# =================================================
class Customer:
    """
    Representasi pelanggan dalam sistem restoran.

    Attributes:
        name (str): Nama pelanggan.
        phone (str): Nomor HP pelanggan.
        people (int): Jumlah orang yang datang.
    """

    def __init__(self, name: str, phone: str, people: int):
        """
        Inisialisasi objek Customer.

        Args:
            name (str): Nama pelanggan.
            phone (str): Nomor HP pelanggan.
            people (int): Jumlah orang.
        """
        self.__name = name
        self.__phone = phone
        self.__people = people

    def get_name(self) -> str:
        """Mengembalikan nama pelanggan."""
        return self.__name

    def get_phone(self) -> str:
        """Mengembalikan nomor HP pelanggan."""
        return self.__phone

    def get_people(self) -> int:
        """Mengembalikan jumlah orang dari pelanggan."""
        return self.__people

    def set_phone(self, new_phone: str):
        """
        Mengubah nomor HP pelanggan.

        Args:
            new_phone (str): Nomor HP baru.
        """
        self.__phone = new_phone


# =================================================
# Kelas Menu
# =================================================
class Menu:
    """
    Representasi item menu makanan/minuman.

    Attributes:
        menu_id (int): ID menu.
        name (str): Nama menu.
        price (int): Harga item menu.
    """

    def __init__(self, menu_id: int, name: str, price: int):
        """
        Inisialisasi objek Menu.

        Args:
            menu_id (int): ID menu.
            name (str): Nama menu.
            price (int): Harga menu.
        """
        self.menu_id = menu_id
        self.name = name
        self.price = price

    def __str__(self):
        """Format string saat objek Menu dicetak."""
        return f"{self.menu_id}. {self.name} - Rp{self.price}"


# =================================================
# Base class Entity
# =================================================
class Entity:
    """
    Kelas dasar untuk entitas yang memiliki relasi dengan Customer.

    Attributes:
        customer (Customer): Objek customer yang terkait.
    """

    def __init__(self, customer: Customer):
        """
        Args:
            customer (Customer): Pelanggan yang terkait dengan entitas.
        """
        self.customer = customer


# =================================================
# Kelas Reservation
# =================================================
class Reservation(Entity):
    """
    Representasi reservasi meja restoran.

    Attributes:
        customer (Customer): Pelanggan yang melakukan reservasi.
        table_number (int): Nomor meja yang dipesan.
    """

    def __init__(self, customer: Customer, table_number: int):
        """
        Inisialisasi objek reservasi.

        Args:
            customer (Customer): Objek customer.
            table_number (int): Nomor meja.
        """
        super().__init__(customer)
        self.table_number = table_number


# =================================================
# Kelas Order
# =================================================
class Order(Entity):
    """
    Representasi pemesanan menu dari pelanggan.

    Attributes:
        customer (Customer): Pelanggan yang membuat pesanan.
        items (List[Menu]): Daftar item menu yang dipesan.
        table_number (int): Nomor meja pemesan.
    """

    def __init__(self, customer: Customer, items: List[Menu], table_number: int):
        """
        Inisialisasi objek Order.

        Args:
            customer (Customer): Pelanggan yang membuat pesanan.
            items (List[Menu]): Daftar menu.
            table_number (int): Nomor meja.
        """
        super().__init__(customer)
        self.items = items
        self.table_number = table_number

    def total_price(self) -> int:
        """Menghitung total harga seluruh menu yang dipesan."""
        return sum(item.price for item in self.items)

    def print_receipt(self):
        """Menampilkan struk pembayaran dalam format teks."""
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
    """
    Kelas dasar untuk laporan.
    Class ini memberikan struktur polymorphism untuk berbagai jenis laporan.
    """
    def print(self):
        """Method dasar yang wajib dioverride oleh subclass."""
        raise NotImplementedError("Method ini harus dioverride di subclass.")


class TextReport(Report):
    """Laporan dalam bentuk teks biasa."""
    def print(self):
        print("[Laporan Teks] Menampilkan laporan sederhana...")


class DBReport(Report):
    """Laporan yang bersumber dari database."""
    def print(self):
        print("[Laporan Database] Membaca laporan dari database...")


# Buat dokumentasi HTML:
#   py -m pydoc -w models
#
# Buat dokumentasi teks:
#   py -m pydoc models