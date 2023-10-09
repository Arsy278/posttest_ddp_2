import os
os.system('cls')

from prettytable import PrettyTable
daftar_barang = PrettyTable()
daftar_barang.title = "Daftar Sepeda"
daftar_barang.field_names = ["No", "Nama Barang", "Harga", "Stok"]
keranjang_belanja = PrettyTable()
keranjang_belanja.field_names = ["Nama Barang", "Harga", "Jumlah"]

barang = {
    1: {"Nama Barang": "Polygon Xtrada 5", "Harga": 6400000, "Stok": 10},
    2: {"Nama Barang": "Polygon Siskiu D6", "Harga": 14250000, "Stok": 18},
    3: {"Nama Barang": "Polygon Heist X2", "Harga": 10626000, "Stok": 12},
    4: {"Nama Barang": "Polygon Premier 4", "Harga": 6986000, "Stok": 16},
    5: {"Nama Barang": "Polygon Premier 5", "Harga": 8300000, "Stok": 14},
}

for no, data in barang.items():
        daftar_barang.add_row([no, data["Nama Barang"], f"Rp {data['Harga']:,.2f}".replace(",", "."), data["Stok"]])

def tambah_item():
    nama_barang = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))
    
    tambah = len(barang) + 1
    barang[tambah] = {"Nama Barang": nama_barang, "Harga": harga, "Stok": stok}

    daftar_barang.clear_rows()
    for no, data in barang.items():
        daftar_barang.add_row([no, data["Nama Barang"], f"Rp {data['Harga']:,.2f}".replace(",","."), data["Stok"]])
    print("Barang telah ditambahkan ke daftar belanja")

def perbarui_item():
    nomor_item = int(input("Nomor item yang akan diperbarui: "))
    if nomor_item in barang:
        data = barang[nomor_item]
        print(f"Nama Barang: {data['Nama Barang']}")
        print(f"Harga: Rp {data['Harga']}")
        print(f"Stok: {data['Stok']}")
        print("Kosongkan jika tidak ingin mengubah item.")
        nama_barang = input("Masukkan barang baru: ")
        harga = input("harga barang baru: ")
        stok = input("Stok: ")

        if nama_barang:
            data["Nama Barang"] = nama_barang
        if harga:
            data["Harga"] = int(harga)
        if stok:
            data["Stok"] = int(stok)
        print("Barang telah sukses diperbarui.")

        daftar_barang.clear_rows()
        for no, data in barang.items():
            daftar_barang.add_row([no, data["Nama Barang"], f"Rp {data['Harga']:,.2f}".replace(",", "."), data["Stok"]])
        print(daftar_barang)
    else:
        print("Nomor item tidak sesuai. Silahkan pilih ulang opsi.")

def hapus_item():
    pilihan = int(input("Masukkan nomor item yang ingin dihapus: "))
    if pilihan in barang:
        del barang[pilihan]
        print("Barang berhasil dihapus.")

        daftar_barang.clear_rows()
        for no, data in barang.items():
                daftar_barang.add_row([no, data["Nama Barang"], f"Rp {data['Harga']:,.2f}".replace(",", "."), data["Stok"]])
        print(daftar_barang)
    else:
        print("Masukkan nomor item yang benar")

data_admin = {
    "Nama Admin": "arsy",
    "ID": "1234"
}

print(f"{'-'*40:^40}")
print(f"{'Toko Sepeda Alam Citra':^40}")
print(f"{'-'*40:^40}")
print("1. Admin")
print("2. Pembeli")
print("3. Keluar")
opsi = input("Siapa yang mengakses program ini? (1/2/3): ")


if opsi == "1":
    x = input("Nama Admin : ")
    y = input("ID : ")
    if x == data_admin["Nama Admin"] and y == data_admin["ID"]:
        print(f"{'-'*40:^40}")
        print(f"{'Toko Sepeda Alam Citra':^40}")
        print(f"{'-'*40:^40}")

        while True:
            exit_program = False
            print("\nPilih opsi Admin:")
            print("1. Tambah Item")
            print("2. Tampilkan Daftar Harga Sepeda")
            print("3. Perbarui Item")
            print("4. Hapus Item")
            print("5. Keluar")
                
            pilihan = input("\nPilih opsi (1/2/3/4/5): ")
            if pilihan == "1":
                tambah_item()
            if pilihan == "2":
                print(daftar_barang)
            if pilihan == "3":
                perbarui_item()
            if pilihan == "4":
                hapus_item()
            if pilihan == "5":
                print(f"{'-'*40:^40}")
                print(f"{'Terima Kasih !':^40}")
                print(f"{'-'*40:^40}")
                exit_program = True
                break
while True:
    exit_program = False
    if opsi == "2":
        def beli_item():
            nomor_item = int(input("Nomor item yang ingin dibeli: "))
            if nomor_item in barang:
                data = barang[nomor_item]
                print(f"Anda akan membeli {data['Nama Barang']} seharga Rp {data['Harga']:,.2f}".replace(",", "."))
                jumlah = int(input("Jumlah yang ingin dibeli: "))
                if jumlah <= data['Stok']:
                    data['Stok'] -= jumlah
                    keranjang_belanja.add_row([data['Nama Barang'], f" Rp {data['Harga']:,.2f}".replace(",", "."), jumlah])
                    print(f"{jumlah} {data['Nama Barang']} telah ditambahkan ke keranjang belanja.")
                else:
                    print(f"Maaf, stok {data['Nama Barang']} tidak mencukupi.")
            else:
                print("Nomor item tidak valid.")
                    
        print("\nPilih opsi:")
        print("1. Beli")
        print("2. Lihat Keranjang")
        print("3. Keluar")
            
        pilihan = input("\nPilih opsi (1/2/3): ")
        if pilihan == "1":
            print(daftar_barang)
            beli_item()
        elif pilihan == "2":
            print("Keranjang Belanja: ")
            print(keranjang_belanja)
        elif pilihan == "3":
            print(f"{'-'*40:^40}")
            print(f"{'Terima Kasih Sudah Berbelanja !':^40}")
            print(f"{'-'*40:^40}")
            break
        exit_program = True
