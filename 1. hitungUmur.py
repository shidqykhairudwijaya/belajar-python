tahunPengguna = int(input("Input tahun Lahir kamu:"))
tahunSekarang = 2025


if tahunPengguna > tahunSekarang or tahunPengguna <= 0:
    print("Tahun lahir tidak valid  ")
else:
    hasil = tahunSekarang - tahunPengguna
    print(f"Umur kamu adalah:{hasil} tahun")