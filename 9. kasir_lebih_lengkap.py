def tampilkan_menu(menu):
    i = 1
    for key, values in menu.items():
        print(f"{i}. {key}: {values}")
        i += 1
    print("Selesai (tulis)")



def pesanan(menu, listnya):
    berhenti = True
    total_satu_barang = 0
    while berhenti:
        
        pesanan_user = input("Pilih menu: ").title()
        if pesanan_user in menu:
            jumlah = int(input("Jumlah: "))
            if jumlah <= 0:
                print("Jumlah tidak valid!")
            else:
                total_satu_barang = menu[pesanan_user] * jumlah
                listnya.append({
                    "Nama": pesanan_user,
                    "Jumlah": jumlah,
                    "Total": total_satu_barang
                })
        elif pesanan_user.lower() == "selesai":
            listnya.sort(key=lambda x: (x["Total"]), reverse=True)
            berhenti = False
        else:
            print("Input tidak valid!")

def struk(listnya):
    total_semuanya = 0
    for i in listnya:
        total_semuanya += i["Total"]
    print("======  STRUK BELANJA ======")
    for i in listnya:
        print(f"{i['Nama']} x {i['Jumlah']} = Rp. {i['Total']}")
    print("----------------------------")
    print(f"Subtotal     = {total_semuanya}")

    diskon = 0
    if total_semuanya >= 100000:
        diskon = 10
    elif total_semuanya >= 50000 and total_semuanya < 100000:
        diskon = 5
    diskon_total = total_semuanya * diskon/100
    print (f"Diskon ({diskon}%)  = Rp. {diskon_total}")

    ppn = 0.11
    total_ppn = total_semuanya * ppn
    print(f"PPN (11%)    = Rp. {total_ppn}")
    total = total_semuanya - diskon_total + total_ppn
    print(f"----------------------------")
    print(f"Total Akhir = Rp. {int(total):,}")

def main():
    listnya = []
    daftar_menu = {
        "Mie Goreng": 10000,
        "Ayam Goreng": 15000,
        "Teh Gelas": 2000
    }

    tampilkan_menu(daftar_menu)
    pesanan(daftar_menu,listnya)
    struk(listnya)

main()