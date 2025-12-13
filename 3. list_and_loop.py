numbers_user = list(map(int, input("Input numbers: ").split()))
 
total = sum(numbers_user)
avg = total / len(numbers_user)

print(f"Total:{total}")
print(f"Rata-rata:{avg}")

"""
input() → membaca input pengguna
.split() → memecah berdasarkan spasi
map(int, ...) → mengubah setiap elemen menjadi integer
list(...) → menyimpannya dalam satu variabel berbentuk list
"""