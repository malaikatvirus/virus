# List untuk menyimpan data karyawan
data_karyawan = []

# Fungsi untuk menambahkan karyawan (Create)
def tambah_karyawan():
    print("\n=== Tambah Data Karyawan ===")
    id_karyawan = input("Masukkan ID Karyawan: ")
    nama = input("Masukkan Nama Karyawan: ")
    posisi = input("Masukkan Posisi Karyawan: ")
    gaji = input("Masukkan Gaji Karyawan: ")

    # Membuat dictionary untuk data karyawan baru
    karyawan_baru = {
        "ID": id_karyawan,
        "Nama": nama,
        "Posisi": posisi,
        "Gaji": gaji
    }

    # Menambahkan ke list
    data_karyawan.append(karyawan_baru)
    print(f"\nKaryawan {nama} berhasil ditambahkan!\n")

# Fungsi untuk menampilkan semua data karyawan (Read)
def tampilkan_karyawan():
    print("\n=== Daftar Data Karyawan ===")
    if not data_karyawan:
        print("Belum ada data karyawan.\n")
        return

    for karyawan in data_karyawan:
        print(f"ID     : {karyawan['ID']}")
        print(f"Nama   : {karyawan['Nama']}")
        print(f"Posisi : {karyawan['Posisi']}")
        print(f"Gaji   : {karyawan['Gaji']}")
        print("-" * 30)
    print()

# Fungsi untuk mengupdate data karyawan (Update)
def update_karyawan():
    print("\n=== Update Data Karyawan ===")
    id_update = input("Masukkan ID Karyawan yang akan diupdate: ")
    for karyawan in data_karyawan:
        if karyawan["ID"] == id_update:
            print("Data sebelum update:")
            print(karyawan)
            # Meminta data baru dari pengguna
            karyawan["Nama"] = input("Masukkan Nama Baru: ")
            karyawan["Posisi"] = input("Masukkan Posisi Baru: ")
            karyawan["Gaji"] = input("Masukkan Gaji Baru: ")
            print("Data karyawan berhasil diupdate!\n")
            return
    print("Karyawan dengan ID tersebut tidak ditemukan.\n")

# Fungsi untuk menghapus data karyawan (Delete)
def hapus_karyawan():
    print("\n=== Hapus Data Karyawan ===")
    id_hapus = input("Masukkan ID Karyawan yang akan dihapus: ")
    for i, karyawan in enumerate(data_karyawan):
        if karyawan["ID"] == id_hapus:
            del data_karyawan[i]
            print(f"Karyawan dengan ID {id_hapus} berhasil dihapus!\n")
            return
    print("Karyawan dengan ID tersebut tidak ditemukan.\n")

# Fungsi untuk menampilkan menu dan memilih opsi
def menu():
    while True:
        print("=== Menu Utama ===")
        print("1. Tambah Karyawan")
        print("2. Tampilkan Karyawan")
        print("3. Update Karyawan")
        print("4. Hapus Karyawan")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == "1":
            tambah_karyawan()
        elif pilihan == "2":
            tampilkan_karyawan()
        elif pilihan == "3":
            update_karyawan()
        elif pilihan == "4":
            hapus_karyawan()
        elif pilihan == "5":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Menjalankan program
if __name__ == "__main__":
    menu()
