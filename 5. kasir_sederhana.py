menu = {
    "nasi goreng": 10000,
    "mie goreng": 12000,
    "es teh": 3000,
    "es jeruk": 5000
}

print("Daftar Menu")
i = 1
for key, values in menu.items(): 
    print(f"{i}. {key}: {values}")
    i += 1

total = 0
while True:
    makanan = input("Input makanan: ")
    if makanan in menu:
        total += menu[makanan]
        selesai = input("Selesai(y/n): ")
        if selesai == "y":
            print(f"total: {total}")
            break
    else:
        print("Menu tidak tersedia")

