tahunPengguna = int(input("Input tahun Lahir kamu ugh:"))
tahunSekarang = 2026


if tahunPengguna > tahunSekarang or tahunPengguna <= 0:
    print("Tahun lahir tidak valid  ")
else:
    hasil = tahunSekarang - tahunPengguna
    print(f"Umur kamu adalah:{hasil} tahun")