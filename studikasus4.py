produk = {
    "nama": "kaset Blur - Parklife",
    "harga": 150000,
    "stok": 5
}

while True:
    print("\n=== MENU DATA PRODUK ===")
    print("1. tampilkan data")
    print("2. tambah kategori")
    print("3. ubah harga")
    print("4. hapus kategori") 
    print("5. keluar")

    pilihan = input("pilih menu: ")

    if pilihan == "1":
        print("\ndata produk: ")
        print(produk)

    elif pilihan == "2":
        kategori = input("masukkan kategori: ")
        produk["kategori"] = kategori
        print("kategori berhasil ditambahkan. ")

    elif pilihan == "3":
        harga_baru = int(input("masukkan harga baru: "))
        produk["harga"] = harga_baru
        print("harga berhasil diubah.")

    elif pilihan == "4":
        if "kategori" in produk:
            del produk["kategori"]
            print("kategori berhasil dihapus.")
        else:
            print("data kategori tidak ada.")

    elif pilihan == "5":
        print("\nprogram selesai.")
        print("data produk setelah perubahan:")
        print(produk)
        break

    else:
        print("pilihan tidak tersedia.")