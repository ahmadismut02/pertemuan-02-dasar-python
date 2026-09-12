"""
Program: Kalkulator Koordinat
Nama   : [Nama Anda]
NIM    : [NIM Anda]
Deskripsi: Menhitung jarak Euclidean, selisih koordinat, dan titik tengah antara dua titik.
"""

# Input koordinat titik A dan B sebagai float
x1 = float(input("Masukkan x1 (Titik A): "))
y1 = float(input("Masukkan y1 (Titik A): "))
x2 = float(input("Masukkan x2 (Titik B): "))
y2 = float(input("Masukkan y2 (Titik B): "))

# Perhitungan selisih koordinat
dx = x2 - x1
dy = y2 - y1

# Perhitungan jarak Euclidean
jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

# Perhitungan titik tengah
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2

# Output hasil perhitungan terformat (2 angka desimal)
print("\n--- Hasil Perhitungan ---")
print(f"Titik A      : ({x1:.2f}, {y1:.2f})")
print(f"Titik B      : ({x2:.2f}, {y2:.2f})")
print(f"Selisih dx   : {dx:.2f}")
print(f"Selisih dy   : {dy:.2f}")
print(f"Jarak        : {jarak:.2f}")
print(f"Titik Tengah : ({mid_x:.2f}, {mid_y:.2f})")