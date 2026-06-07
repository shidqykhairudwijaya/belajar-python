angka = int(input("Masukan angka:"))

blangan = ""
bilangan1 = ""
if angka % 2 == 0:
    bilangan = "genap"
else:
    bilangan = "ganjil"

if angka <= 0:
    bilangan1 = "negatif"
else:
    bilangan1 = "positif"

print(f"{angka} adalah bilangan {bilangan} dan {bilangan1}")