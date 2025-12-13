menu = {
    "Paket 1gb": 3000,
    "Paket 50gb": 50000,
    "Paket 3gb": 10000
}

items = []

i = 1
#menampilkan menu
for key, values in menu.items():
    print(f"{i}. {key} : {values}")
    i += 1
print("selesai")

lanjut = True

total_keseluruhan = 0
while lanjut:
    pilih = input("Pilih: ")
    
    if pilih in menu:
        jumlah = int(input("Jumlah: "))
        if jumlah <= 0:
            print("Jumlah tidak valid!")
        else:
            total_per_barang = menu[pilih] * jumlah
            #cara menambah list dic
            items.append({
                "Nama": pilih,
                "Jumlah": jumlah,
                "Total_barang": total_per_barang,
            })
            #cara operasi di dalam list
            total_keseluruhan = sum(item["Total_barang"] for item in items)
    elif pilih.lower() == "selesai":
        lanjut = False
    else:
        print("Input tidak valid!")

print("=== STRUK BELANJA ===")
for i in items:
    print(f"{i['Nama']} x{i['Jumlah']} = Rp. {i['Total_barang']}")
print("---------------------")
print(f"Total Akhir = Rp. {total_keseluruhan}")