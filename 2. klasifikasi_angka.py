angka = int(input("Masukan angka:"))

if angka > 0:
    if angka % 2 == 0:
        print("Angka positif")
        print("Angka genap")
    else:
        print("Angka positif")
        print("Angka ganjil")
elif angka < 0:
    if angka % 2 == 0:
        print("Angka negatif")
        print("Angka genap")
    else:
        print("Angka negatif")
        print("Angka ganjil")
else:
    print("Angka nol")
    print("Nol tidak ganjil atau genap")