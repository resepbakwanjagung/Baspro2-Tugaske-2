nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Tetap/Honor): ").capitalize()
golongan = input("Masukkan Golongan (A/B/C): ").upper()

if status == "Tetap":
    gaji_pokok = 1000000
    if golongan == "A":
        bonus = 200000
    elif golongan == "B":
        bonus = 400000
    elif golongan == "C":
        bonus = 550000
    else:
        print("Golongan tidak valid!")
        exit()
elif status == "Honor":
    gaji_pokok = 750000
    if golongan == "A":
        bonus = 150000
    elif golongan == "B":
        bonus = 275000
    elif golongan == "C":
        bonus = 480000
    else:
        print("Golongan tidak valid!")
        exit()
else:
    print("Status tidak valid!")
    exit()

gaji_total = gaji_pokok + bonus

print("\n=== Rincian Gaji ===")
print(f"Nama       : {nama}")
print(f"NIK        : {nik}")
print(f"Status     : {status}")
print(f"Golongan   : {golongan}")
print(f"Gaji Pokok : Rp {gaji_pokok:,}")
print(f"Bonus      : Rp {bonus:,}")
print(f"Gaji Total : Rp {gaji_total:,}")