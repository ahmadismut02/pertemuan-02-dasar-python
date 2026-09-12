TAHUN_SEKARANG = 2026

# Menerima input dari pengguna
nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun lahir: "))

# Menghitung umur
umur = TAHUN_SEKARANG - tahun_lahir

# Menampilkan hasil dengan f-string
print(f"\nNama  : {nama}")
print(f"NIM   : {nim}")
print(f"Kelas : {kelas}")
print(f"Umur  : sekitar {umur} tahun")