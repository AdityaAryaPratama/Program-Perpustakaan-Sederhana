data_buku = [{
        'Id Buku' : 'A0001',
        'Judul' : 'Si Putih',
        'Tahun Terbit' : '2021',
        'Genre' : 'Fiction', 
        'Peminjam' : 'Tere Liye'
    },
    {
        'Id Buku' : 'A0002',
        'Judul' : 'Refrain',
        'Tahun Terbit' : '2009',
        'Genre' : 'Romantic Comedy', 
        'Peminjam' : 'Winna Effendi'
    },
    {
        'Id Buku' : 'A0003',
        'Judul' : 'Off The Record',
        'Tahun Terbit' : '2017',
        'Genre' : 'Non Fiction', 
        'Peminjam' : 'Ria SW'
    }]

def menu_func():
    while True:
        # Menampilkan menu opsi program -- capstone
        Menu = input(''' 
        PROGRAM PERPUSTAKAAN DESA TAMBUHAN
        Berikut daftar menu data inventory buku : 
        1. Menu Menampilkan Buku
        2. Menu Menambahkan Buku
        3. Menu Mengubah Data Buku
        4. Menu Menghapus Data Buku
        5. Keluar
        Masukkan angka menu yang ingin dijalankan : 
        ''')
        # User input selain pilihan menu
        

        if (Menu == '1'):
            read_func()
        elif (Menu == '2'):
            create_func()
        elif (Menu == '3'):
            update_func()
        elif (Menu == '4'):
            delete_func()
        elif (Menu == '5'):
            exit() # END
        else:
            print('\nLakukan input sesuai instruksi!\n') # Notifikasi "Pilihan yang anda masukkan salah"
            continue

# Read Data
def read_func():
    inp_read = True
    while True:
        print('''
        Menu Menampilkan Daftar Buku
        1. Tampilkan Daftar Buku
        2. Mencari Buku
        3. Keluar dari menu
        ''') # Tampil Menu Menampilkan Data
        inp_read = input('Silahkan Pilih Sub Menu Daftar Buku [1-3] : ')
        if inp_read == '1': # User pilih opsi 1
            if len(data_buku) != 0: # Ada data
                print('Daftar Buku :') 
                for j, i in enumerate(data_buku): # Menampilkan seluruh data
                    print(f"{j+1}. Id Buku : {i['Id Buku']}, Judul : {i['Judul']}, Tahun Terbit : {i['Tahun Terbit']}, Genre : {i['Genre']}, Peminjam : {i['Peminjam']}")
            else:
                print('\nData tidak tersedia!') # Notifikasi tidak ada data
            continue
        elif inp_read == '2': # User pilih opsi 2
            if len(data_buku) != 0: # Ada data
                Id = input('Masukkan Id Buku : ') # User input prim-key
                print(f'Data Buku dengan Kode : {Id}')
                for j, i in enumerate(data_buku):
                    if i['Id Buku'] == Id: # Ada data
                        print(f"{j+1}. Id Buku : {i['Id Buku']}, Judul : {i['Judul']}, Tahun Terbit : {i['Tahun Terbit']}, Genre : {i['Genre']}, Peminjam : {i['Peminjam']}")
                        # Menampilkan data sesuai input user
                        break
                else:
                    print('\nData tidak ditemukan!') # Notifikasi tidak ada data
                    read_func()  
        elif inp_read == '3': # User pilih opsi 3
                menu_func() # Exit
        else:
            print('\nLakukan input sesuai instruksi!')
    return

# Create Data
def create_func():
    inp_create = True
    while True:
        print('''
        Menu Tambah Data
        1. Tambah Data Buku
        2. Kembali ke Menu Utama
        ''') # Tampil menu menambahkan data
        inp_create = input('Silahkan Pilih Sub Menu Tambah Data [1-2] : ')
        if inp_create == '1': # User pilih opsi 1
            Id = input('Masukkan Id Buku : ') # User input prim-key data
            for j, i in enumerate(data_buku):
                if len(data_buku) != 0:
                    if i['Id Buku'] == Id: # Data duplikat
                        print('Data Sudah Ada') # Notifikasi data sudah ada
                        create_func()
            else:

                peminjam = input('Masukkan Nama : ')
                judul = input('Masukkan Judul : ')
                thn_terbit = input('Masukkan Tahun Terbit : ')
                genre = input('Masukkan Genre : ')
                # User input data (Kelengkapan data)
                while True:
                    conf_create = input('Apakah Data akan disimpan? (Yes/No) : ') # Menampilkan menu pilihan simpan data
                    conf_create = conf_create.lower()
                    if conf_create == 'yes':
                        data_buku.append({'Id Buku' : Id, 'Judul' : judul, 'Tahun Terbit' : thn_terbit, 'Peminjam' : peminjam, 'Genre' : genre})
                        # Menyimpan data
                        print('Data Berhasil Disimpan') # Notifikasi "data tersimpan"
                        create_func()
                    elif conf_create == 'no':
                        print('Data Tidak Disimpan')
                        create_func()
                    else:
                        continue

            break
        elif inp_create == '2':
            menu_func()
        else:
            print('\nLakukan input sesuai instruksi!')
    return

# Update Data
def update_func():
    inp_update = True
    while True:
        print('''
        Menu Ubah Data
        1. Ubah data buku
        2. Kembali ke Menu Utama
        ''') # Tampil menu mengubah data
        inp_update = input('Silahkan Pilih Sub Menu Ubah Data [1-2] : ')
        if inp_update == '1': # User pilih opsi 1
            id = input('Masukkan Id Buku : ' ) # User input prim-key data
            for j, i in enumerate(data_buku):
                if i['Id Buku'] == id: # Ada data
                    print(f"{j+1}. Id Buku : {i['Id Buku']}, Judul : {i['Judul']}, Tahun Terbit : {i['Tahun Terbit']}, Genre : {i['Genre']}, Peminjam : {i['Peminjam']}")
                    # Menampilkan data sesuai prim-key data
                    while True:
                        conf_id = input('Apakah data akan dilanjutkan melakukan update? (Yes/No) : ') # Lanjut data
                        conf_id = conf_id.lower()
                        if conf_id == 'yes':
                            while True:
                                col_update = input('Masukkan kolom yang ingin diedit : ') 
                                col_update = col_update.lower()
                                if col_update == 'Id': # User input kolom yang akan di update
                                    idBaru = input('Masukkan ID baru : ') # User input value baru
                                    while True:
                                        conf_update = input('Apakah data akan diupdate? (Yes/No) : ') # Update data
                                        conf_update = conf_update.lower()
                                        if conf_update == "yes":
                                            data_buku[j]["Id"] = idBaru # Mengupdate data
                                            print("\nData berhasil diubah") # Notifikasi data terupdate
                                            break
                                        elif conf_update == 'no':
                                            print('\nData gagal diubah')
                                            break 
                                        else:
                                            continue
                                    break
                                elif col_update == 'peminjam': # User input kolom yang akan di update
                                    peminjamBaru = input('Masukkan nama baru : ') # User input value baru
                                    while True:
                                        conf_update = input('Apakah data akan diupdate? (Yes/No) : ') # Update data
                                        conf_update = conf_update.lower()
                                        if conf_update == "yes":
                                            data_buku[j]["Peminjam"] = peminjamBaru # Mengupdate data
                                            print("\nData berhasil diubah") # Notifikasi data terupdate
                                            break
                                        elif conf_update == 'no':
                                            print('\nData gagal diubah')
                                            break 
                                        else:
                                            continue
                                    break
                                elif col_update == 'tahun terbit':
                                    thnBaru = input('Masukkan kelas Baru : ')
                                    while True:
                                        conf_update = input('Apakah data akan diupdate? (Yes/No) : ')
                                        conf_update = conf_update.lower()
                                        if conf_update == "yes":
                                            data_buku[j]["Tahun Terbit"] = thnBaru
                                            print("Data berhasil diubah")
                                            break
                                        elif conf_update == 'no':
                                            print('Data tidak diupdate')
                                            menu_func()
                                        else:
                                            continue
                                    break
                                elif col_update == 'judul':
                                    judulBaru = input('Masukkan judul Baru : ')
                                    while True:
                                        conf_update = input('Apakah data akan diupdate? (Yes/No) : ')
                                        conf_update = conf_update.lower()
                                        if conf_update == "yes":
                                            data_buku[j]["Judul"] = judulBaru
                                            print("Data berhasil diubah")
                                            break
                                        elif conf_update == 'no':
                                            print('Data gagal diubah')
                                            break
                                        else:
                                            continue
                                    break
                                elif col_update == 'genre':
                                    genreBaru = input('Masukkan genre baru : ')
                                    while True:
                                        conf_update = input('Apakah data akan diupdate? (Yes/No) : ')
                                        conf_update = conf_update.lower()
                                        if conf_update == "yes":
                                            data_buku[j]["Genre"] = genreBaru
                                            print("Data berhasil diupdate")
                                            break
                                        elif conf_update == 'no':
                                            print('Data tidak diupdate')
                                            break
                                        else:
                                            continue       
                                    break
                                else:
                                    print('\nKolom tidak ditemukan!\n')
                                    break
                            break
                        elif col_update == 'no':
                            print('\nData Tidak Jadi Diupdate')    
                            break
                        else:
                            continue
                    break        
            else:
                print('\nData Tidak Ditemukan!')
                continue
        elif inp_update == '2':
            menu_func()
        else:
            print('\nLakukan input sesuai instruksi!')
    return

def delete_func():
    inp_del = True
    while True:
        print('''
        Menu Hapus Data Buku
        1. Hapus data buku
        2. Kembali ke Menu Utama
        ''') # Tampil menu hapus data
        inp_del = input('Silahkan Pilih Sub Menu Hapus Data [1-2] : ')
        if inp_del == '1': # User pilih opsi 1
            id = input('Masukkan id buku : ') # User input prim-key data
            for j, i in enumerate(data_buku):
                if i['Id Buku'] == id: # Ada data
                    print(f"{j+1}. Id Buku : {i['Id Buku']}, Judul : {i['Judul']}, Tahun Terbit : {i['Tahun Terbit']}, Genre : {i['Genre']}, Peminjam : {i['Peminjam']}")
                    while True:
                        conf_del = input('Apakah Data akan Dihapus? (Yes/No) : ') # Menampilkan menu pilihan hapus data
                        conf_del = conf_del.lower()
                        if conf_del == 'yes': # Hapus data
                            data_buku[j]['Id Buku'] == id
                            del data_buku[j] # Menghapus data
                            print('\nData berhasil dihapus') # Notifikasi "Data Deleted"
                            break
                        elif conf_del == 'no':
                            print('\nData tidak dihapus')
                            break # Tampil menu menghapus data
                        else:
                            continue
                    break
            else:
                print('Data Tidak Ditemukan!') # Notifikasi "Data yang anda cari tidak ada"
                continue
        elif inp_del == '2':
            menu_func() # Exit
        else:
            print('\nLakukan input sesuai instruksi!')
    return


menu_func()



