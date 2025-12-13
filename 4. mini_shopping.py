daftar = {
    "Nasi goreng": 10000,
    "Mie goreng": 20000,
    "Teh gelas": 3000
}

print("Daftar Menu")
i = 1
for key, values in daftar.items():
    print(f"{i}. {key}: {values}")
    i += 1

total = 0
while True:
    input_user = input("Pilih makanan:")
    if input_user in daftar:
        total += daftar[input_user]
    else:
        print("Menu tidak tersedia")
    validasi = input("Pilih lagi(y/n): ")
    if validasi.lower() == "n":
        break
    
print(f"Total harga:Rp. {total}")



