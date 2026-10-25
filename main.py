from database import buat_tabel, koneksi_database
def hitung_hpp():
    print("\n================================")
    print("          HITUNG HPP")
    print("================================")

    nama_produk = input("Nama produk: ")

    biaya_bahan = float(input("Biaya bahan baku: "))
    biaya_kemasan = float(input("Biaya kemasan: "))
    biaya_tenaga = float(input("Biaya tenaga kerja: "))
    biaya_lainnya = float(input("Biaya lainnya: "))

    jumlah_produksi = int(input("Jumlah produksi: "))

    total_biaya = (
        biaya_bahan
        + biaya_kemasan
        + biaya_tenaga
        + biaya_lainnya
    )

    hpp = total_biaya / jumlah_produksi

    keuntungan = float(input("Target keuntungan (%): "))

    harga_jual = hpp + (hpp * keuntungan / 100)

    print("\n================================")
    print("             HASIL")
    print("================================")
    print(f"Produk           : {nama_produk}")
    print(f"Total biaya      : Rp{total_biaya:,.0f}")
    print(f"HPP per produk   : Rp{hpp:,.0f}")
    print(f"Keuntungan       : {keuntungan:.0f}%")
    print(f"Harga jual       : Rp{harga_jual:,.0f}")
    print("================================")

def tambah_produk():
    print("\n================================")
    print("          TAMBAH PRODUK")
    print("================================")

    nama = input("Nama produk: ")
    harga_jual = float(input("Harga jual: "))
    stok = int(input("Stok awal: "))
    hpp = float(input("HPP produk: "))

    koneksi = koneksi_database()
    cursor = koneksi.cursor()

    cursor.execute("""
        INSERT INTO produk (nama, harga_jual, stok, hpp)
        VALUES (?, ?, ?, ?)
    """, (nama, harga_jual, stok, hpp))

    koneksi.commit()
    koneksi.close()

    print("\nProduk berhasil ditambahkan.")

def lihat_produk():
    print("\n================================")
    print("           DATA PRODUK")
    print("================================")

    koneksi = koneksi_database()
    cursor = koneksi.cursor()

    cursor.execute("SELECT * FROM produk")
    produk = cursor.fetchall()

    koneksi.close()

    if not produk:
        print("Belum ada produk.")
        return

    print(f"{'ID':<5} {'Nama':<20} {'Harga':<15} {'Stok':<10} {'HPP'}")
    print("-" * 65)

    for item in produk:
        print(
            f"{item[0]:<5} "
            f"{item[1]:<20} "
            f"Rp{item[2]:<12,.0f} "
            f"{item[3]:<10} "
            f"Rp{item[4]:,.0f}"
        )

def menu_produk():
    while True:
        print("\n================================")
        print("          DATA PRODUK")
        print("================================")
        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Kembali")
        print("================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_produk()

        elif pilihan == "2":
            lihat_produk()

        elif pilihan == "3":
            break

        else:
            print("Pilihan tidak tersedia.")

buat_tabel()

while True:
    print("\n================================")
    print("          UMKM MANAGER")
    print("================================")
    print("1. Data Produk")
    print("2. Hitung HPP")
    print("3. Penjualan")
    print("4. Pengeluaran")
    print("5. Laporan")
    print("6. Keluar")
    print("================================")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        menu_produk()

    elif pilihan == "2":
        hitung_hpp()

    elif pilihan == "3":
        print("\n=== PENJUALAN ===")
        print("Fitur belum dibuat.")

    elif pilihan == "4":
        print("\n=== PENGELUARAN ===")
        print("Fitur belum dibuat.")

    elif pilihan == "5":
        print("\n=== LAPORAN ===")
        print("Fitur belum dibuat.")

    elif pilihan == "6":
        print("\nTerima kasih telah menggunakan UMKM Manager.")
        break

    else:
        print("\nPilihan tidak tersedia.")