### Capstone Modul 1 Fatah Wiksa Adristo

## Konteks : Manajemen inventaris / koleksi museum.
## Problem : museum memiliki banyak barang yang belum terlacak dan tidak rapi.
## Task : membuat sistem agar museum dapat menyimpan koleksi dengan rapi dan menjadikannya
## lebih mudah untuk menambahkan, menghapus, merubah, atau melihat koleksi yang ada di museum.
## Limitasi : setelah keluar dari program, data koleksi yang telah diubah tidak dapat disimpan.

# Data Collection Type (dictionary dalam list) : data berisi ID item yang terdiri dari tahun ditambahkan, nama item, kategori item, dan angka unik maksimal 3 digit
inventory = [
    {"item_ID":"2016FOS001", "nama":"Mammoth Fossil", "kategori": "Fossil", "berat": 300, "kondisi": "Restorasi", "tahun_masuk": 2016, "estimasi_nilai": 45000},
    {"item_ID":"2001FOS001", "nama":"Komodo Fossil", "kategori": "Fossil", "berat": 70, "kondisi": "Rusak", "tahun_masuk": 2001, "estimasi_nilai": 1500},
    {"item_ID":"2018ART001", "nama":"Kapak Genggam", "kategori": "Artifact", "berat": 7, "kondisi": "Rusak", "tahun_masuk": 2018, "estimasi_nilai": 400},
    {"item_ID":"2022ROC001", "nama":"Pyrite", "kategori": "Rocks", "berat": 15, "kondisi": "Display", "tahun_masuk": 2022, "estimasi_nilai": 600},
    {"item_ID":"1999ROC001", "nama":"Obsidian", "kategori": "Rocks", "berat": 10, "kondisi": "Display", "tahun_masuk": 1999, "estimasi_nilai": 750}
]

header = f"| {"ID Item":<15} | {"Nama Item":<26}| {"Kategori": <15}| {"Berat":<8}| {"Kondisi":<10} | {"Tahun Masuk":<8} | {"Estimasi Nilai":<12} |"
lebar_tabel = 118

# Membuat infinite loop untuk menu aplikasi
while True:
    mainMenu = input('''
Selamat Datang di Sistem Manajemen Penyimpanan Museum A
========================================================
Silahkan Pilih Salah Satu dari Pilihan Berikut
                     
Menu Utama:
1. Menampilkan Inventaris Museum
2. Menambah Data Baru ke Inventaris Museum
3. Menghapus Data dari Inventaris Museum
4. Merubah Data dari Inventaris Museum
5. Keluar
Input Anda: ''')

    # Menampilkan inventaris museum
    if mainMenu == "1":
        while True:
            print('''
Menu Read Aplikasi:
1. Tampilkan Keseluruhan Inventaris
2. Tampilkan Berdasarkan Kategori
3. Pencarian Berdasarkan ID
0. Keluar Dari Menu
            ''')
            menuRead = input("Input nomor menu yang ingin dipilih: ")
            if menuRead == "1":
                while True:
                    print("Inventaris Museum".center(lebar_tabel))  # judul dari menu read
                    print("="*lebar_tabel) # border
                    print(header) # header tabel read
                    print("="*lebar_tabel) #border
                    total_nilai = 0                        
                    for i in range(len(inventory)):
                        print(f"| {inventory[i]["item_ID"]:<15} | {inventory[i]["nama"]:<25} | {inventory[i]["kategori"]:<15}| {inventory[i]["berat"]:>8}| {inventory[i]["kondisi"]:<10} | {inventory[i]["tahun_masuk"]:<11} | {inventory[i]["estimasi_nilai"]:>14} |") # menambahkan data dari data collection ke tabel
                        total_nilai += inventory[i]['estimasi_nilai']
                    print("="*lebar_tabel)
                    print(f"Jumlah koleksi: {len(inventory)} item")
                    print(f"Total estimasi nilai aset: ${total_nilai}") 
                    print("\n0. Keluar dari menu")   
                    tombol = input("Input '0' jika ingin keluar: ") #input untuk user memilih untuk keluar dari menu, jika tidak "0", maka muncul prompt bahwa input tidak valid
                    if tombol == "0":
                        break
                    else:
                        print("Input yang dimasukkan tidak valid.")
            
            elif menuRead == "2":
                while True:
                    readKategori = input("Input kategori yang ingin ditampilkan: ").capitalize()
                    found = False
                    
                    print(f"\nInventaris Kategori: {readKategori}".center(118))
                    print("="*lebar_tabel)
                    print(header)
                    print("="*lebar_tabel)
                    
                    for i in range(len(inventory)):
                        if inventory[i]["kategori"].capitalize() == readKategori:    # membandingkan input user dengan value di kolom "kategori"
                            print(f"| {inventory[i]['item_ID']:<15} | {inventory[i]['nama']:<25} | {inventory[i]['kategori']:<15}| {inventory[i]['berat']:>8}| {inventory[i]['kondisi']:<10} | {inventory[i]['tahun_masuk']:<11} | {inventory[i]['estimasi_nilai']:>14} |")
                            found = True
                    if not found:
                        print(f"Item dengan kategori '{readKategori}' tidak ditemukan.".center(118))
                    
                    print("="*lebar_tabel)

                    while True:                                                             # membuat infinite loop untuk menu tambahan baru
                        print('''
Apakah ingin mencari kategori lain?
1. Cari kategori lain
0. Keluar menu
                              ''')
                        tombol = input("Input pilhan anda: ")
                        
                        if tombol == "1":
                            break                                                              # mengembalikan ke menu tambahan item
                        elif tombol == "0":
                            break                                                              # keluar dari loop ke menu 1
                        else:
                            print("Input tidak valid.")                   # karena tidak ada break, lanjut ke menu pilihan
                    if tombol == "0":
                        break   

            elif menuRead == "3":
                while True:
                    readID = input("Input ID Item yang dicari: ").upper()
                    found = False
                    
                    for i in range(len(inventory)):
                        if inventory[i]["item_ID"].strip() == readID:
                            print(f"\nData Item ID: {readID}".center(118))
                            print("="*lebar_tabel)
                            print(header)
                            print("="*lebar_tabel)
                            print(f"| {inventory[i]['item_ID']:<15} | {inventory[i]['nama']:<25} | {inventory[i]['kategori']:<15}| {inventory[i]['berat']:>8}| {inventory[i]['kondisi']:<10} | {inventory[i]['tahun_masuk']:<11} | {inventory[i]['estimasi_nilai']:>14} |")
                            print("="*lebar_tabel)
                            found = True
                            break 
                    
                    if not found:
                        print(f"Item dengan ID '{readID}' tidak ditemukan.".center(118))

                    while True:                                                             # membuat infinite loop untuk menu tambahan baru
                        print('''
Apakah ingin mencari item lain?
1. Cari item lain
0. Keluar menu
                              ''')
                        tombol = input("Input pilihan anda: ")
                        
                        if tombol == "1":
                            break                                                              # mengembalikan ke menu tambahan item
                        elif tombol == "0":
                            break                                                              # keluar dari loop ke menu 1
                        else:
                            print("Input tidak valid.")                   # karena tidak ada break, lanjut ke menu pilihan
                    if tombol == "0":
                        break   
            elif menuRead == "0":
                break
            else:
                print("Input tidak ada dalam menu. Silakan diulang.")
                
        
            

    # Menambahkan stok baru ke inventaris museum
    elif mainMenu == "2":
        while True:
            item_baru = input("Input nama item baru: ").capitalize()             # user input nama item yang baru
            kategori_baru = input("Input kategori item baru: ").capitalize()     # user input kategori item baru
            while True:
                berat_baru = input("Input berat item baru (kg): ")               # user input berat item baru
                if berat_baru.isdigit():
                    break
                else:
                    print("Input harus dalam integer / angka")
            kondisi_baru = input("Input kondisi item baru (Rusak/Restorasi/Display): ").capitalize()       # user input kondisi item baru
            while True:
                tahun_masuk_baru = input("Input tahun masuk item: ")             # user input berat item baru
                if tahun_masuk_baru.isdigit():
                    break
                else:
                    print("Input tahun harus dalam integer / angka")
            while True:
                estimasi_nilai_baru = input("Input estimasi nilai item ($): ")   # user input nilai item baru
                if estimasi_nilai_baru.isdigit():
                    break
                else:
                    print("Input nilai harus dalam integer / angka")
            id_dasar = f"{tahun_masuk_baru}{kategori_baru[:3].upper()}" # menambahkan ID baru dari tahun, 3 huruf pertama nama item, 3 huruf pertama kategori
            is_duplicate = True
            if is_duplicate:
                unique_id = 1
                for item in inventory:
                    if item["item_ID"].strip().startswith(id_dasar):    # menambahkan ID unik dibelakang ID dasar yang terdiri dari 3 digit
                        unique_id += 1
                id_baru = f"{id_dasar}{unique_id:03}" 
                while True:
                    print(f'''
Anda akan menambahkan {item_baru} dengan ID {id_baru},
1. Tambah item
0. Kembali ke menu sebelumnya
    ''')
                    checker1 = input("Input pilihan anda: ")
                    if checker1 == "1":
                        inventory.append({"item_ID": id_baru, 
                                        "nama": item_baru, 
                                        "kategori": kategori_baru, 
                                        "berat": int(berat_baru), 
                                        "kondisi": kondisi_baru, 
                                        "tahun_masuk": int(tahun_masuk_baru), 
                                        "estimasi_nilai": int(estimasi_nilai_baru)
                                        }) # menambahkan item yang baru ke dalam tabel yang baru
                        print("Inventaris Museum".center(lebar_tabel))  # judul dari menu read
                        print("="*lebar_tabel)              # border
                        print(header) # header tabel read
                        print("="*lebar_tabel)
                        for i in range(len(inventory)):
                            print(f"| {inventory[i]["item_ID"]:<15} | {inventory[i]["nama"]:<25} | {inventory[i]["kategori"]:<15}| {inventory[i]["berat"]:>8}| {inventory[i]["kondisi"]:<10} | {inventory[i]["tahun_masuk"]:<11} | {inventory[i]["estimasi_nilai"]:>14} |") # menambahkan data dari data collection ke tabel
                        print("="*lebar_tabel) 
                        break
                    elif checker1 == "0":
                        break
                    else:
                        print("Input tidak valid.")
                        break
                if checker1 == "0":
                    break
            
            while True:                                                             # membuat infinite loop untuk menu tambahan baru
                print('''
Apakah ingin menambah item lain?
1. Tambah item lain
0. Keluar menu
                              ''')
                tombol = input("Input pilihan anda: ")
                
                if tombol == "1":
                    break                                                              # mengembalikan ke menu tambahan item
                elif tombol == "0":
                    break                                                              # keluar dari loop ke menu 2
                else:
                    print("Input tidak valid.")                   # karena tidak ada break, lanjut ke menu pilihan
            if tombol == "0":
                break                                                                  # keluar ke menu utama

    # Menghapus data yang ada pada data collection
    elif mainMenu == "3":
        while True:
            print("Inventaris Museum".center(lebar_tabel))  # judul dari menu read
            print("="*lebar_tabel)              # border
            print(header) # header tabel read
            print("="*lebar_tabel)
            for i in range(len(inventory)):
                print(f"| {inventory[i]["item_ID"]:<15} | {inventory[i]["nama"]:<25} | {inventory[i]["kategori"]:<15}| {inventory[i]["berat"]:>8}| {inventory[i]["kondisi"]:<10} | {inventory[i]["tahun_masuk"]:<11} | {inventory[i]["estimasi_nilai"]:>14} |") # menambahkan data dari data collection ke tabel
            print("="*lebar_tabel) 

            hapus_id = input("Masukkan ID item yang ingin dihapus (ketik 0 untuk membatalkan): ").upper()
            if hapus_id == "0":
                break               # kembali ke menu 3 jika batal menghapus
            found = False 
            hapus_index = -1
            for i in range(len(inventory)):         # menghapus item dari IDnya, loop untuk mengecek apakah input sama dengan ID yang ada di data collection
                if inventory[i]["item_ID"].strip() == hapus_id:
                    hapus_index = i
                    found = True
                    break
                
            if found:
                nama_terhapus = inventory[hapus_index]["nama"]
                while True:
                    print(f'''
Anda akan menghapus {nama_terhapus} dengan ID {hapus_id},
1. Hapus item
0. Kembali ke menu sebelumnya
''')
                    checker2 = input("Input pilihan anda: ")
                    if checker2 == "1":
                        print(f"\nItem '{nama_terhapus}' dengan ID {hapus_id} berhasil dihapus!")
                        inventory.pop(hapus_index)
                        break
                    elif checker2 == "0":
                        print("Penghapusan batal.")
                        break
                    else:
                        print("Input tidak valid.")
            else:
                print(f"Item dengan ID {hapus_id} tidak ditemukan.")
            while True:                                                             # membuat infinite loop untuk menu tambahan baru
                print('''
Apakah anda ingin menghapus item lain?
1. Hapus item lain
0. Keluar menu
                    ''')
                tombol = input("Input pilihan anda: ")
                
                if tombol == "1":
                    break                                                              # mengembalikan ke menu tambahan item
                elif tombol == "0":
                    break                                                              # keluar dari loop ke menu 3
                else:
                    print("Input tidak valid.")                   # karena tidak ada break, lanjut ke menu pilihan
            if tombol == "0":
                break        

    # Merubah parameter pada data
    elif mainMenu == "4":
        while True:
            print("Inventaris Museum".center(lebar_tabel))  # judul dari menu read
            print("="*lebar_tabel)              # border
            print(header) # header tabel read
            print("="*lebar_tabel)
            for i in range(len(inventory)):
                print(f"| {inventory[i]["item_ID"]:<15} | {inventory[i]["nama"]:<25} | {inventory[i]["kategori"]:<15}| {inventory[i]["berat"]:>8}| {inventory[i]["kondisi"]:<10} | {inventory[i]["tahun_masuk"]:<11} | {inventory[i]["estimasi_nilai"]:>14} |") # menambahkan data dari data collection ke tabel
            print("="*lebar_tabel)

            ubah_item = input("Input ID item yang akan diubah (input 0 untuk keluar): ").upper() # input untuk memasukkan ID item yang akan diubah
            if ubah_item == "0":
                print("Kembali ke menu utama.")
                break

            index_item = -1
            for i in range(len(inventory)):     # jika parameter index_item berubah, item dapat diubah, jika tidak berarti ID tidak ditemukan
                if inventory[i]["item_ID"].strip().upper() == ubah_item:
                    index_item = i
                    break

            if index_item == -1:
                print("ID item tidak ditemukan. Silahkan dicoba lagi.")
                continue

            print('''
Daftar Kolom yang Bisa Diubah:
1. Kondisi
2. Kategori
0. Keluar
                ''')            # menu perubahan
            kolom_ubah = input("Input nomor kolom yang akan diubah: ")

            if kolom_ubah == "1":
                key_ubah = "kondisi"
            elif kolom_ubah == "2":
                key_ubah = "kategori"
            elif kolom_ubah == "0":
                print("Kembali ke menu utama.")
                break
            else:
                print("Input tidak valid.")
                continue

            value_ubahan = input(f"Masukkan {key_ubah} baru: ").capitalize()      # input untuk merubah parameter ubahan
            
            while True:
                print(f'''
Anda akan merubah {key_ubah} menjadi {value_ubahan},
1. Simpan perubahan
0. Kembali ke menu sebelumnya
''')
                checker3 = input("Input pilihan anda: ")
                if checker3 =="1":
                    if key_ubah == "kategori":                                            # merubah kategori, dikarenakan kategori termasuk parameter ID item, ID juga diubah
                        kategori_awal = inventory[index_item]["kategori"]

                        if value_ubahan != kategori_awal:
                            
                            tahun = inventory[index_item]["tahun_masuk"]
                            nama = inventory[index_item]["nama"]
                            id_dasar_update = f"{tahun}{value_ubahan[:3].upper()}"        # ID awal (belum ada 3 angka di belakang)

                            id_unik_update = 0
                            for item in inventory:
                                if item["item_ID"].startswith(id_dasar_update):                             # menambahkan ID unik
                                    id_unik_update += 1                                                     
                            inventory[index_item]["kategori"] = value_ubahan                    
                            id_baru_update = f"{id_dasar_update}{(id_unik_update+1):03}"                    # menggabungkan ID awal dengan ID unik 3 digit (string)
                            inventory[index_item]["item_ID"] = id_baru_update
                            print(f"ID item telah diperbarui menjadi: {id_baru_update}")
                        else:
                            print("Kategori sama dengan sebelumnya. ID tidak berubah")
                    elif key_ubah == "kondisi":
                        inventory[index_item]["kondisi"] = value_ubahan
                    print(f"Item {inventory[index_item]["nama"]} telah diubah.")
                    break
                elif checker3 =="0":
                    print("Perubahan dibatalkan.")
                    break
                else:
                    print("Input tidak valid.")
            while True:                                                             # membuat infinite loop untuk menu tambahan baru
                print('''
Apakah ingin merubah kategori lain?
1. Ubah item lain
0. Keluar menu
                            ''')
                tombol = input("Input pilihan anda: ")
                
                if tombol == "1":
                    break                                                              # mengembalikan ke menu tambahan item
                elif tombol == "0":
                    break                                                              # keluar dari loop ke menu 4
                else:
                    print("Input tidak valid.")                   # karena tidak ada break, lanjut ke menu pilihan
            if tombol == "0":
                break           

    # Keluar dari aplikasi
    elif mainMenu == "5":
        print("Terima kasih! Anda telah keluar dari program.")
        break
    else:
        print("Pilihan tidak ada di menu. Silahkan diulang.")