def hitung_bmi(berat_badan, tinggi_badan):
    bmi = berat_badan / (tinggi_badan ** 2)
    return bmi

def tampilkan_info(berat_badan, tinggi_badan, bmi):
    print("Berat Badan Anda adalah:", berat_badan, "Kg")
    print("Tinggi Badan Anda adalah:", tinggi_badan, "M")
    print("BMI Anda adalah:", bmi)

def keterangan_bmi(bmi):
    if bmi < 18.5:
        print("Berat badan kurang")
    elif 18.5 <= bmi < 24.9:
        print("Berat badan normal")
    elif 25 <= bmi < 29.9:
        print("Kelebihan berat badan")
    else:
        print("Obesitas")
