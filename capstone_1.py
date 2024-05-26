############################## DATABASE BUKU ################################

# Applikasi Database Peminjaman Buku Perpustakaan ABC
# Tahap pertama kita akan membuat sebuah dictionary yang akan menampung seluruh informasi dari data sebuah buku yang ada di perpustakaan
daftar_buku = {
1:  {
        'ID Buku': 'NO001',
        'Genre': 'Novel  ',
        'Judul': "Harry Potter and The Sorcerer's Stone",
        'Penulis': 'J.K. Rowling',
        'Stok': 10
    },
2:  {
        'ID Buku': 'NO002',
        'Genre': 'Novel  ',
        'Judul': 'Harry Potter and The Chamber of Secrets',
        'Penulis': 'J.K. Rowling',
        'Stok': 15
    },
3:  {
        'ID Buku': 'FA003',
        'Genre': 'Fantasi',
        'Judul': 'Bumi',
        'Penulis': 'Tere Liye',
        'Stok': 18
    },
4:  {
        'ID Buku': 'FA004',
        'Genre': 'Fantasi',
        'Judul': 'Negeri Para Bedebah',
        'Penulis': 'Tere Liye',
        'Stok': 9
    },
5:  {
        'ID Buku': 'RO005',
        'Genre': 'Roman  ',
        'Judul': 'Ancika: Dia Yang Bersamaku Tahun 1995',
        'Penulis': 'Pidi Baiq',
        'Stok': 5
    },
6:  {
        'ID Buku': 'FI006',
        'Genre': 'Fiksi  ',
        'Judul': 'Laut Bercerita',
        'Penulis': 'Leila Salikha Chudori',
        'Stok': 2
    }
}

# mengubah Dictionary menjadi sebuah list
list_buku = [value for key, value in daftar_buku.items()]

# Daftar peminjaman buku
peminjaman_buku = []
   
########################## DEF SUBMENU UTAMA ####################################

# Show Book List Function | Submenu dari READ
def show_list_buku(data):
    print('\n' + '-' * 44 + ' Daftar Buku ' + '-' * 44 )
    print(f' {"ID Buku":<10} | {"Genre":<10} | {"Judul":<40} | {"Penulis":<21} | {"Stok":<5}')
    print(' ' + '-' * 100)
    for i in range(len(data)):
        print(f' {data[i]["ID Buku"]:<10} | {data[i]["Genre"]:<10} | {data[i]["Judul"]:<40} | {data[i]["Penulis"]:<21} | {data[i]["Stok"]:<5}')       
# :<10 berarti lebar kolom adalah 10 karakter dan teks akan diratakan ke kiri.
# :<40 berarti lebar kolom adalah 40 karakter dan teks akan diratakan ke kiri.
# :<21 berarti lebar kolom adalah 20 karakter dan teks akan diratakan ke kiri.
# :<5 berarti lebar kolom adalah 5 karakter dan teks akan diratakan ke kiri.

# Fungsi untuk menampilkan daftar peminjam
def show_list_peminjaman(data):
    print('\n' + '-' * 44 + ' Daftar Peminjam ' + '-' * 44)
    print(f' {"Borrower ID":<15} | {"ID Buku":<10} | {"Lama Pinjam":<12} | {"Judul Buku":<40} | {"Jumlah Pinjam":<5}')
    print(' ' + '-' * 100)
    for peminjaman in data:
        print(f' {peminjaman["borrower_id"]:<15} | {peminjaman["ID Buku"]:<10} | {peminjaman["Lama Waktu Pinjam"]:<12} | {peminjaman["Judul Buku"]:<40} | {peminjaman["Jumlah Pinjam"]:<5}')
# :<15 berarti lebar kolom adalah 10 karakter dan teks akan diratakan ke kiri.
# :<10 berarti lebar kolom adalah 40 karakter dan teks akan diratakan ke kiri.
# :<12 berarti lebar kolom adalah 20 karakter dan teks akan diratakan ke kiri.
# :<5 berarti lebar kolom adalah 5 karakter dan teks akan diratakan ke kiri

# Search Function | Submenu dari READ
def author_search(nama_penulis):
    return [buku for buku in list_buku if nama_penulis.lower() in buku['Penulis'].lower()]

# Title Search Function | Submenu dari READ
def title_search(nama_judul):
    return [buku for buku in list_buku if nama_judul.lower() in buku['Judul'].lower()]
    
# Fungsi untuk mengupdate genre, judul, dan penulis | Submenu dari UPDATE
def update_genre_judul_penulis(buku):
    buku['Genre'] = input(f"Masukkan Genre Baru ({buku['Genre']}): ") or buku['Genre']
    buku['Judul'] = input(f"Masukkan Judul Baru ({buku['Judul']}): ") or buku['Judul']
    buku['Penulis'] = input(f"Masukkan nama Penulis Baru ({buku['Penulis']}): ") or buku['Penulis']
    print("Genre, Judul, dan Penulis berhasil diupdate!")
    
# Fungsi untuk mengupdate stok buku | Submenu dari UPDATE
def update_stok(buku):
    buku['Stok'] = int(input(f"Masukkan Stok Baru ({buku['Stok']}): ") or buku['Stok'])
    print("Stok buku berhasil diupdate!")

############################# DEF MENU UTAMA #####################################

# READ MENU 
def read():
    sub_menu_read = (int(input('''                                         
Buku apa yang ingin Anda cari:
1. Tampilkan semua buku 
2. Masukan nama penulis
3. Masukan nama judul buku
4. Kembali ke menu utama
Masukan angka yang diinginkan: ''')))
    if sub_menu_read == 1:
        show_list_buku(list_buku)
    elif sub_menu_read == 2:
        nama_penulis = input('Masukan nama Penulis: ')
        hasil = author_search(nama_penulis)
        if hasil:
            show_list_buku(hasil)
        else:
            print('Maaf, nama Penulis yang Anda maksud tidak ada')
    elif sub_menu_read == 3:
        nama_judul = input('Masukan judul buku: ')
        hasil = title_search(nama_judul)
        if hasil:
            show_list_buku(hasil)
        else:
            print('Maaf, judul buku yang Anda cari tidak ada')
    elif sub_menu_read == 4:
        return
    else:
        print('Mohon maaf pilihan Anda tidak valid')

# UPDATE MENU
def update_book():
    id_buku = input("Masukkan ID Buku yang akan diupdate: ")
    for buku in list_buku:
        if buku['ID Buku'] == id_buku:
            while True:
                sub_menu_update = int(input('''
                Pilih opsi yang ingin diupdate:
                1. Update Genre, Judul, dan Penulis
                2. Update Stok buku
                3. Kembali ke menu utama
                Masukkan angka yang diinginkan: '''))
                if sub_menu_update == 1:
                    update_genre_judul_penulis(buku)
                elif sub_menu_update == 2:
                    update_stok(buku)
                elif sub_menu_update == 3:
                    return
                else:
                    print('Pilihan tidak valid, silakan coba lagi.')
            return
    print("ID Buku tidak ditemukan!")
            
# ADD MENU
def add_book():
    temp_list = list_buku.copy()
    show_list_buku(temp_list)  # Menampilkan daftar buku terlebih dahulu
    while True:
        id_buku = input("Masukkan ID Buku: ")
        if any(buku['ID Buku'] == id_buku for buku in temp_list):
            print("ID Buku sudah ada, silakan masukkan ID Buku yang berbeda.")
        else:
            break
    genre = input("Masukkan Genre Buku: ")
    judul = input("Masukkan Judul Buku: ")
    penulis = input("Masukkan Penulis Buku: ")
    stok = int(input("Masukkan Stok Buku: "))
    new_book = {'ID Buku': id_buku, 'Genre': genre, 'Judul': judul, 'Penulis': penulis, 'Stok': stok}
    temp_list.append(new_book)
    show_list_buku(temp_list)  # Menampilkan daftar buku setelah penambahan
    konfirmasi = input("Apakah Anda ingin menyimpan perubahan? (Ya/Tidak): ")
    if konfirmasi.lower() == 'ya':
        list_buku.append(new_book)
        print("Buku berhasil ditambahkan!")
    else:
        print("Perubahan dibatalkan.")

# DELETE MENU
def delete_book():
    temp_list = list_buku.copy()
    show_list_buku(temp_list)  # Menampilkan daftar buku terlebih dahulu
    id_buku = input("Masukkan ID Buku yang akan dihapus: ")
    for buku in temp_list:
        if buku['ID Buku'] == id_buku:
            temp_list.remove(buku)
            show_list_buku(temp_list)  # Menampilkan daftar buku setelah penghapusan
            konfirmasi = input("Apakah Anda ingin menyimpan perubahan? (Ya/Tidak): ")
            if konfirmasi.lower() == 'ya':
                list_buku.remove(buku)
                print("Buku berhasil dihapus!")
            else:
                print("Perubahan dibatalkan.")
            return
    print("ID Buku tidak ditemukan!")

# Fungsi untuk meminjam buku
def borrow_book():
    show_list_buku(list_buku)  # Menampilkan daftar buku terlebih dahulu
    borrower_id = input("Masukkan ID peminjam: ")
    nama_judul = input("Masukkan judul buku yang ingin dipinjam: ")
    lama_pinjam = int(input("Masukkan lama waktu pinjaman (hari): "))

    for buku in list_buku:
        if buku['Judul'].lower() == nama_judul.lower():
            if buku['Stok'] == 0:
                print('Stok buku habis')
                return
            else:
                jumlah_pinjam = int(input("Masukkan jumlah buku yang ingin dipinjam: "))
                if jumlah_pinjam > buku['Stok']:
                    print(f'Stok buku tidak mencukupi. Sisa stok buku {buku["Judul"]}: {buku["Stok"]}')
                    return
                else:
                    buku['Stok'] -= jumlah_pinjam
                    peminjaman_buku.append({
                        'borrower_id': borrower_id,
                        'ID Buku': buku['ID Buku'],
                        'Lama Waktu Pinjam': lama_pinjam,
                        'Judul Buku': buku['Judul'],
                        'Jumlah Pinjam': jumlah_pinjam
                    })
                    print(f'Buku "{buku["Judul"]}" berhasil dipinjam!')
                    show_list_peminjaman(peminjaman_buku)  # Menampilkan hasil akhir dari peminjaman buku
                    return
    print("Judul buku tidak ditemukan!")

# Fungsi untuk mengembalikan buku
def return_book():
    show_list_peminjaman(peminjaman_buku)  # Menampilkan daftar peminjam terlebih dahulu
    borrower_id = input("Masukkan ID peminjam: ")
    for peminjaman in peminjaman_buku:
        if peminjaman['borrower_id'] == borrower_id:
            for buku in list_buku:
                if buku['ID Buku'] == peminjaman['ID Buku']:
                    buku['Stok'] += peminjaman['Jumlah Pinjam']
                    peminjaman_buku.remove(peminjaman)
                    print(f'Buku "{buku["Judul"]}" berhasil dikembalikan!')
                    show_list_peminjaman(peminjaman_buku)  # Menampilkan hasil akhir dari peminjaman buku
                    return
    print("Data peminjam tidak ditemukan!")
            
################################# MENU UTAMA #####################################

# Menu utama berisikan berbagai macam menu yang bisa user pilih5
# Fungsi untuk menampilkan menu utama
def menu_utama():
    while True:
        pilih_menu = int(input('''
Selamat datang di Perpustakaan ABC
Silahkan memilih salah satu menu berikut:
                               
1. Pencarian Buku
2. Mengubah Daftar Buku
3. Menambah Daftar Buku
4. Hapus Daftar Buku
5. Peminjaman Buku
6. Pengembalian Buku
7. Tampilkan Daftar Peminjam
8. Keluar
                               
Masukkan angka dari menu yang Anda inginkan: '''))
        if pilih_menu == 1:
            read()
        elif pilih_menu == 2:
            update_book()
        elif pilih_menu == 3:
            add_book()
        elif pilih_menu == 4:
            delete_book()
        elif pilih_menu == 5:
            borrow_book()
        elif pilih_menu == 6:
            return_book()
        elif pilih_menu == 7:
            show_list_peminjaman(peminjaman_buku)
        elif pilih_menu == 8:
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

################################# JALANKAN CODE ##################################

# Menjalankan menu utama
menu_utama()

        

    
        

        