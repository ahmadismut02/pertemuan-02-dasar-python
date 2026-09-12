KELVIN_OFFSET = 273.15

# Menerima input suhu Celsius sebagai float
celsius = float(input("Masukkan suhu Celsius: "))

# Perhitungan konversi suhu
fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

# Menampilkan hasil
print(f"Fahrenheit : {fahrenheit:.2f}")
print(f"Kelvin     : {kelvin:.2f}")