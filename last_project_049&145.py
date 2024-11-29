barang = [
    {"nama": "Barang A", "harga": 10000},
    {"nama": "Barang B", "harga": 15000},
    {"nama": "Barang C", "harga": 20000}
]

keranjang = []


def tampilkan_barang():
    if len(barang) == 0:
        print("Tidak ada barang yang tersedia.")
    else:
        print("Daftar Barang:")
        for urutan, data in enumerate(barang):
            print(f"{urutan}. Nama: {data['nama']}, Harga: {data['harga']}")

def tampilkan_keranjang(total_harga=0):
    if len(keranjang) == 0:
        print("Keranjang belanja kosong.")
    else:
        print("Isi Keranjang Belanja: ")
        total_harga = 0  
        for urutan, item in enumerate(keranjang):
            harga_total_item = item["harga"] * item["jumlah"]
            total_harga += harga_total_item
            print(f"{urutan}. Nama: {item['nama']}, Harga: {item['harga']}, Jumlah: {item['jumlah']}, Total: {harga_total_item}")
        print(f"Total Belanja: {total_harga}")
    
    return total_harga




def tambah_keranjang():
    tampilkan_barang()
    pilihan_barang = input("Pilih nomor barang yang ingin ditambah ke keranjang (atau -1 untuk membatalkan): ")
    
    if pilihan_barang == "-1":
        return

    if not pilihan_barang.isdigit():
        print("Input tidak valid. Harap masukkan angka.")
        return
    
    pilihan_barang = int(pilihan_barang)

    if pilihan_barang < 0 or pilihan_barang >= len(barang):
        print("Nomor barang tidak valid.")
        return
    
    jumlah_beli = input("Masukkan jumlah yang ingin dibeli: ")
    
    if not jumlah_beli.isdigit():
        print("Input tidak valid. Harap masukkan angka.")
        return
    
    jumlah_beli = int(jumlah_beli)
    if jumlah_beli <= 0:
        print("Jumlah beli tidak valid.")
        return


    keranjang.append({
        "nama": barang[pilihan_barang]["nama"],
        "harga": barang[pilihan_barang]["harga"],
        "jumlah": jumlah_beli
    })
    print(f"{jumlah_beli} {barang[pilihan_barang]['nama']} telah ditambahkan ke keranjang.")


def update_keranjang():
    tampilkan_keranjang()
    pilihan_item = input("Pilih nomor barang di keranjang yang ingin diupdate (atau -1 untuk membatalkan): ")
    
    if pilihan_item == "-1":
        return

    if not pilihan_item.isdigit():
        print("Input tidak valid. Harap masukkan angka.")
        return
    
    pilihan_item = int(pilihan_item)

    if pilihan_item < 0 or pilihan_item >= len(keranjang):
        print("Nomor item di keranjang tidak valid.")
        return
    
    jumlah_baru = input("Masukkan jumlah baru untuk item ini: ")
    
    if not jumlah_baru.isdigit():
        print("Input tidak valid. Harap masukkan angka.")
        return

    jumlah_baru = int(jumlah_baru)
    if jumlah_baru <= 0:
        print("Jumlah baru tidak valid.")
        return
    

    keranjang[pilihan_item]['jumlah'] = jumlah_baru
    print(f"Jumlah {keranjang[pilihan_item]['nama']} di keranjang telah diubah menjadi {jumlah_baru}.")


def hapus_dari_keranjang():
    tampilkan_keranjang()
    pilihan_item = input("Pilih nomor barang di keranjang yang ingin dihapus (atau -1 untuk membatalkan): ")
    
    if pilihan_item == "-1":
        return

    if not pilihan_item.isdigit():
        print("Input tidak valid. Harap masukkan angka.")
        return
    
    pilihan_item = int(pilihan_item)

    if pilihan_item < 0 or pilihan_item >= len(keranjang):
        print("Nomor item di keranjang tidak valid.")
        return
    
    # Menghapus barang dari keranjang
    item_dihapus = keranjang.pop(pilihan_item)
    print(f"{item_dihapus['nama']} telah dihapus dari keranjang.")

# Fungsi untuk menghitung total pembayaran
def pembayaran(total_harga=0):
    member = input("Apakah anda memiliki member? (ya / tidak) ")
    pembayaran = int(input("Masukkan jumlah uang yang dibayar: "))
    while pembayaran < total_harga:
        print("Harap Masukan uang lebih supaya barang dapat dibeli. ")
        pembayaran = int(input("Masukkan jumlah uang yang dibayar: "))

    donasi = input("Apakah Anda Ingin mendonasikan semua kembalian anda? (ya / tidak) ")
    print()
    print("-------------------------------------- Nota Pembelian -------------------------------------- ")

    # Menampilkan daftar barang yang dibeli
    tampilkan_keranjang()

    if member.lower() == 'ya':
        diskon = total_harga * 0.10
        total_diskon = total_harga - diskon
        print(f"Potongan Harga: {diskon}")
        print(f"Total Bayar   : {total_diskon}")
    else:
        print(f"Potongan Harga: -")
        print(f"Total Bayar   : {total_harga}")

    if member.lower() == "ya":
        kembalian = pembayaran - total_diskon
        print(f"Kembalian     : {kembalian}")
    else:
        kembalian = pembayaran - total_harga
        print(f"Kembalian     : {kembalian}")

    if kembalian > 0:
        if donasi.lower() == "ya":
            print(f"kembalian anda sebesar {kembalian}, kami donasikan")

    print("Terima kasih sudah Berkunjung!")
    keranjang.clear()




def menu():
    while True:
        print("\nSistem Kasir untuk Pembeli")
        print("1. Tampilkan Barang")
        print("2. Tampilkan Keranjang")
        print("3. Tambah Barang ke Keranjang")
        print("4. Update Keranjang Belanja")
        print("5. Hapus Barang dari Keranjang")
        print("6. Lakukan pembayaran dan akhiri belanja")
        
        pilihan = input("Pilih menu (1-6): ")
        print("=========================================")
        print()

        if not pilihan.isdigit():
            print("Pilihan menu tidak valid. Harap masukkan angka antara 1-5.")
            continue
        
        pilihan = int(pilihan)
        
        if pilihan == 1:
            tampilkan_barang()

        elif pilihan == 2:
            total_harga = tampilkan_keranjang(0)

        elif pilihan == 3:
            tambah_keranjang()

        elif pilihan == 4:
            update_keranjang()

        elif pilihan == 5:
            hapus_dari_keranjang()

        elif pilihan == 6:
            total_harga = tampilkan_keranjang()
            pembayaran(total_harga)
            break

menu()