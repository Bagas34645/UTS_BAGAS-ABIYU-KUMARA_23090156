import modul

berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (m): "))

bmi = modul.hitung_bmi(berat_badan, tinggi_badan)

modul.tampilkan_info(berat_badan, tinggi_badan, bmi)

modul.keterangan_bmi(bmi)
