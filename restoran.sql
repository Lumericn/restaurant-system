-- Active: 1744248802338@@127.0.0.1@3306
-- ======================================================
-- 1. CREATE DATABASE
-- ======================================================
CREATE DATABASE IF NOT EXISTS restoran;
USE restoran;

-- ======================================================
-- 2. TABLE: reservations (pemesanan meja)
-- ======================================================
CREATE TABLE IF NOT EXISTS reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    people INT NOT NULL,
    table_number INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ======================================================
-- 3. TABLE: menu_items (daftar menu)
-- ======================================================
CREATE TABLE IF NOT EXISTS menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price INT NOT NULL
);

INSERT INTO menu_items (name, price) VALUES
('Nasi Goreng', 20000),
('Ayam Geprek', 18000),
('Es Teh Manis', 5000),
('Jus Alpukat', 15000);

-- ======================================================
-- 4. TABLE: orders
-- ======================================================
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    table_number INT NOT NULL,
    total_price INT DEFAULT 0,
    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ======================================================
-- 5. TABLE: order_items
-- ======================================================
CREATE TABLE IF NOT EXISTS order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    menu_id INT NOT NULL,
    quantity INT DEFAULT 1,
    price INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (menu_id) REFERENCES menu_items(id)
);