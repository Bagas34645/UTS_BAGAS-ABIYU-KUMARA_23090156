import modul

berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (m): "))

bmi = modul.hitung_bmi(berat_badan, tinggi_badan)

print("Berat Badan Anda adalah:", berat_badan, "Kg")
print("Tinggi Badan Anda adalah:", tinggi_badan, "M")
print("BMI Anda adalah:", bmi)

if bmi < 18.5:
    print("Berat badan kurang")
elif 18.5 <= bmi < 24.9:
    print("Berat badan normal")
elif 25 <= bmi < 29.9:
    print("Kelebihan berat badan")
else:
    print("Obesitas")
