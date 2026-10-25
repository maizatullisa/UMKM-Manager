import sqlite3
import os


def koneksi_database():
    return sqlite3.connect("umkm.db")


def buat_tabel():
    koneksi = koneksi_database()
    cursor = koneksi.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produk (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            harga_jual REAL NOT NULL,
            stok INTEGER NOT NULL,
            hpp REAL NOT NULL
        )
    """)

    koneksi.commit()
    koneksi.close()

    print("DATABASE BERHASIL DIBUAT")
    print("Lokasi database:", os.path.abspath("umkm.db"))