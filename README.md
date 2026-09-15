# Studi_Kasus_4_Shaina-Naila-Raihana

# PENJELASAN PROGRAM

Program ini dibuat menggunakan bahasa pemograman python untuk mengelola data produk berupa kaset musik. Data produk disimpan menggunakan **Dictionary**, kemudian pengguna dapat menampilkan data, menambahkan kategori, mengubah harga, menghapus kategori, dan keluar dari program melalui menu yang tersedia. 

# 1. Membuat Dictionary 

<img width="313" height="74" alt="Screenshot 2026-09-15 195953" src="https://github.com/user-attachments/assets/18ef9e7b-c3f5-4034-a8f7-04a0b15713e1" />

bagian ini digunakan untuk membuat dictionary bernama produk. dictionary digunakan untuk menyimpan data dalam bentuk key and value

- "nama" merupakan key dengan value "Kaset Blur - Parklife".
- "harga" merupakan key dengan value 150000
- "stok" merupakan key dengan value 5

jadi, data awal produk terdiri dari nama kaset, harga, dan jumlah stok

# 2. Membuat perulangan 

<img width="208" height="39" alt="Screenshot (475)" src="https://github.com/user-attachments/assets/3141af12-b9f7-4acb-8e63-d3d27889dc65" />

while true digunakan untuk membuat program terus berjalan dan menampilkan menu berulang kali dan menampilkan menu berulang kali. perulangan akan berenti ketika user memilih menu 5 (Keluar) dan program menjalankan break.

# 3. Menampilkan Menu

<img width="600" height="178" alt="Screenshot (476)" src="https://github.com/user-attachments/assets/dc089dbf-5daf-4eb2-91e1-3bb076ebab0e" />

Bagian ini digunakan untuk menampilkan pilihan menu yang dapat digunakan oleh user.

menu terdiri dari
- 1 untuk menampilkan data produk
- 2 untuk menambahkan kategori
- 3 untuk mengubah harga
- 4 untuk menghapus kategori
- 5 untuk keluar dari program

# 4 Menerima Pilihan Pengguna

<img width="567" height="89" alt="Screenshot (477)" src="https://github.com/user-attachments/assets/95b6a560-2919-4a2d-b364-7584bd92529c" />

input() digunakan untuk menerima masukan dari user. masukan tersebut disimpan ke dalam variabel pilihan dan digunakan untuk menentukan menu yang akan dijalankan.

# 5. Menampilkan Data Produk

<img width="526" height="94" alt="Screenshot (478)" src="https://github.com/user-attachments/assets/4da9820a-e63e-45aa-a19c-8f7219347d05" />

Jika user memilih menu 1, program akan menampilkan seluruh isi dictionary produk.

# 6. Menambahkan kategori

<img width="772" height="168" alt="Screenshot (479)" src="https://github.com/user-attachments/assets/c0213292-5aff-4962-990e-a054285d1246" />

jika user memilih menu 2, program meminta user memasukkan kategori produk. data tersebut kemudian ditambahkan ke dictionary dengan key "kategori"

# 7. Mengubah Harga

<img width="759" height="125" alt="Screenshot (480)" src="https://github.com/user-attachments/assets/9da453af-2e47-427f-b04b-e19efbd9041c" />

Jika user memilih menu 3, program meminta harga baru. fungsi int() digunakan agar input harga berupa angka.

kemudian:

<img width="357" height="37" alt="Screenshot (480)" src="https://github.com/user-attachments/assets/81ae2ab9-e0e9-42fb-be26-f2d81b86de49" />

digunakan untuk mengganti nilai harga yang sebelumnya tersimpan dalam dictionary.

# 8. Menghapus Kategori

<img width="696" height="180" alt="Screenshot (481)" src="https://github.com/user-attachments/assets/61378315-7270-4dc0-a9b3-6b03155d852d" />

Menu 4 digunakan untuk menghapus kategori

<img width="303" height="34" alt="Screenshot (481)" src="https://github.com/user-attachments/assets/2ba0649a-a459-4be7-b6ae-f96148b260c7" />

digunakan untuk mengecek apakah key "kategori" ada di dalam dictionary

jika ada, perintah:

<img width="291" height="37" alt="Screenshot (482)" src="https://github.com/user-attachments/assets/734525d6-4557-44fa-9a02-f378b3f13fc8" />

akan menghapus kategori tersebut.

jika kategori belum ada, program akan menampilkan pesan "kategori tidak ada."

# 9. Keluar dari program

<img width="674" height="148" alt="Screenshot (483)" src="https://github.com/user-attachments/assets/7dd997c3-3b0d-47f6-b7ff-4b3ece920562" />

jika user memilih menu 5, program akan menampilkan data produk terakhir setelah dilakukan perubahan.

kemudian break digunakan untuk menghentikan perulangan while true, sehingga program selesai dijalankan.

# 10. Pilihan Menu Tidak Sesuai

<img width="568" height="79" alt="Screenshot (484)" src="https://github.com/user-attachments/assets/70ce4f67-aca2-475c-b118-8cb5152fdd7a" />

Bagian else, digunakan jika user memasukkan pilihan selain 1 sampai 5. prohgram akan memberikan pesan bahwa pilihan tersebut tidak tersedia.

# kesimpulan

Program ini menggunakan dictionary, perulangan, percabangan, input, dan operasi dictionary untuk mengelola data produk. dengan program ini, user dapat menampilkan data produk, menambahkan kategori, mengubah harga, menghapus kategori, dan melihat data akhir sebelum program dihentikan.

# HASIL OUTPUT

# menampilkan data

<img width="379" height="140" alt="Screenshot 2026-09-15 205724" src="https://github.com/user-attachments/assets/ccc0aaff-14a8-4482-b909-2071a44b64b7" />

# menambahkan kategori

<img width="296" height="125" alt="Screenshot 2026-09-15 205827" src="https://github.com/user-attachments/assets/30809e3d-c52f-474b-ad38-ea82da7918e7" />

# mengubah harga

<img width="224" height="127" alt="Screenshot 2026-09-15 210111" src="https://github.com/user-attachments/assets/0b3df2b8-d210-4d49-a596-14bf1062dd1b" />

# menghapus kategori

<img width="277" height="140" alt="Screenshot 2026-09-15 210148" src="https://github.com/user-attachments/assets/8e7d530b-63d9-4fa1-8fe1-8d36dce69c0d" />

# Jika pilihan tidak sesuai

<img width="224" height="109" alt="image" src="https://github.com/user-attachments/assets/02613cf1-4f8b-4909-9410-d723a66d06a9" />

# Data akhir

<img width="447" height="164" alt="Screenshot 2026-09-15 210235" src="https://github.com/user-attachments/assets/215bb8f9-c1e3-4632-b47f-9597af2401dc" />
