# Menerima input panjang dan lebar sebagai float
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

# Menghitung luas dan keliling
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Menampilkan hasil dengan 2 angka di belakang koma (.2f)
print(f"Luas     : {luas:.2f}")
print(f"Keliling : {keliling:.2f}")