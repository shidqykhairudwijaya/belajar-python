menu = {
    "Laptop": 2000000,
    "Handphone": 1000000,
    "RAM": 300000,
}

i = 1

for key, values in menu.items():
    print(f"{i}. {key} : Rp. {values}")
    i += 1

print("4. selesai")

lanjut = True

total = 0

while lanjut:
    input_user = input("Pilih Menu:")

    if input_user in menu:
        jumlah = int(input("Jumlah item:"))
        if jumlah < 0:
            print("Jumlah tidak boleh minus")
        else:
            total += menu[input_user] * jumlah  
    elif input_user.lower() == "selesai":
        lanjut = False
    else:
        print("Item tidak tersedia")

print(f"Total: {total}")