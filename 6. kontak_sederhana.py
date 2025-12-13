
def tambah_kontak(daftar_kontak):
    while True:
        nama = input("Input nama: ")
        nomor = input("Input nomor: ")

        daftar_kontak[nama] = nomor
        validasi = input("Tambah lagi(y/n): ")
        if validasi == "n".lower():
            break
    for key, values in daftar_kontak.items():
        print(f"{key}: {values}")

def cari_kontak(daftar_kontak):
    input_user = input("Input nama: ")
    if input_user in daftar_kontak:
        print(f"{input_user}: {daftar_kontak[input_user]}")
    else:
        print("Kontak tidak ditemukan")

def Tampilkan_semua_kontak(daftar_kontak):
    for key, values in daftar_kontak.items():
        print(f"{key}: {values}")

def main():
    daftar_kontak = {}

    while True:
        print("Aplikasi Kontak sederhana")
        print("1. Tambah Kontak")
        print("2. Cari kontak")
        print("3. Lihat semua kontak")
        print("4. keluar")
        
        pilihan = int(input("Input angka di dalam menu: "))

        if pilihan == 1:
            tambah_kontak(daftar_kontak)
        elif pilihan == 2:
            cari_kontak(daftar_kontak)
        elif pilihan == 3:
            Tampilkan_semua_kontak(daftar_kontak)
        elif pilihan == 4:
            print("Semoga hari mu menyenangkan")
            break
        else:
            print("Input salah!")
        print()

main()

    