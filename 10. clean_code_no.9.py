def tampilkan_menu(menu):
    print("\n=== DAFTAR MENU ===")
    for i, (nama, harga) in enumerate(menu.items(), start=1):
        print(f"{i}. {nama} : Rp {harga}")
    print("Ketik 'selesai' untuk checkout\n")


def input_pesanan(menu):
    pesanan = []

    lanjut = True
    while lanjut:
        pilihan = input("Pilih menu: ").title()

        if pilihan in menu:
            jumlah = int(input("Jumlah: "))

            if jumlah <= 0:
                print("Jumlah harus lebih dari 0")
                continue

            subtotal = menu[pilihan] * jumlah
            pesanan.append({
                "nama": pilihan,
                "jumlah": jumlah,
                "subtotal": subtotal
            })

        elif pilihan.lower() == "selesai":
            lanjut = False
        else:
            print("Menu tidak tersedia")

    # urutkan dari subtotal tertinggi
    pesanan.sort(key=lambda x: x["subtotal"], reverse=True)
    return pesanan


def hitung_total(pesanan):
    subtotal = sum(item["subtotal"] for item in pesanan)

    diskon_persen = 0
    if subtotal >= 100_000:
        diskon_persen = 10
    elif subtotal >= 50_000:
        diskon_persen = 5

    diskon = subtotal * diskon_persen / 100
    ppn = subtotal * 0.11
    total_akhir = subtotal - diskon + ppn

    return subtotal, diskon_persen, diskon, ppn, total_akhir


def cetak_struk(pesanan):
    subtotal, diskon_persen, diskon, ppn, total = hitung_total(pesanan)

    print("\n===== STRUK BELANJA =====")
    for item in pesanan:
        print(f"{item['nama']} x{item['jumlah']} = Rp {item['subtotal']:,}")

    print("-------------------------")
    print(f"Subtotal      = Rp {subtotal:,}")
    print(f"Diskon ({diskon_persen}%) = Rp {int(diskon):,}")
    print(f"PPN (11%)     = Rp {int(ppn):,}")
    print("-------------------------")
    print(f"Total Akhir   = Rp {int(total):,}")


def main():
    menu = {
        "Mie Goreng": 10_000,
        "Ayam Goreng": 15_000,
        "Teh Gelas": 2_000
    }

    tampilkan_menu(menu)
    pesanan = input_pesanan(menu)
    cetak_struk(pesanan)


main()
