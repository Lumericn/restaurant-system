import unittest
from unittest.mock import patch, MagicMock
from models import Customer, Menu, Order, Reservation
from function import buat_reservasi as br
from function import buat_pesanan as bp

class TestRestaurantSystem(unittest.TestCase):

    def setUp(self):
        self.menu1 = Menu(1, "Nasi Goreng", 15000)
        self.menu2 = Menu(2, "Teh Manis", 5000)

    def test_customer_creation(self):
        c = Customer("Danu", "081232121112", 2)
        self.assertEqual(c.get_name(), "Danu")
        self.assertEqual(c.get_phone(), "081232121112")
        self.assertEqual(c.get_people(), 2)

    def test_order_total_price(self):
        c = Customer("Danu", "081232121112", 2)
        order = Order(c, [self.menu1, self.menu2], table_number=5)
        self.assertEqual(order.total_price(), 20000)

    def test_reservation_creation(self):
        c = Customer("Danu", "081232121112", 2)
        r = Reservation(c, 5)
        self.assertEqual(r.table_number, 5)
        self.assertEqual(r.customer.get_name(), "Danu")

    # ===================== Test Buat Reservasi =====================
    @patch('function.buat_reservasi.connect_db')
    @patch('function.buat_reservasi.input', side_effect=["Danu", "081232121112", "3", "2"])
    def test_buat_reservasi(self, mock_input, mock_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_db.return_value = mock_conn

        br.buat_reservasi()

        self.assertTrue(mock_cursor.execute.called)
        self.assertTrue(mock_conn.commit.called)
        self.assertTrue(mock_conn.close.called)

    # ===================== Test Buat Pesanan =====================
    @patch('function.buat_pesanan.connect_db')  # pastikan patch sesuai path
    @patch('function.buat_pesanan.input', side_effect=[
        "Danu",            # Nama pelanggan
        "081232121112",    # Nomor HP
        "2",               # Jumlah orang
        "5",               # Nomor meja
        "1,2"              # Pilihan menu
    ])
    def test_buat_pesanan(self, mock_input, mock_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        # Simulasi menu di database
        mock_cursor.fetchall.return_value = [
            (1, "Nasi Goreng", 15000),
            (2, "Teh Manis", 5000)
        ]

        mock_conn.cursor.return_value = mock_cursor
        mock_db.return_value = mock_conn

        # Jalankan fungsi
        bp.buat_pesanan()

        # Pastikan cursor.execute dipanggil minimal satu kali
        self.assertTrue(mock_cursor.execute.called, "Cursor execute tidak pernah dipanggil!")
        self.assertTrue(mock_conn.commit.called, "Commit tidak pernah dipanggil!")
        self.assertTrue(mock_conn.close.called, "Close tidak pernah dipanggil!")

if __name__ == "__main__":
    unittest.main()
