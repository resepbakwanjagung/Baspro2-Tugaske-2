def hitung_gaji(nama, nik, status, golongan):
    
    gaji = {"Tetap": 1000000, "Honor": 750000}
    bonus = {
        "Tetap": {"A": 200000, "B": 400000, "C": 550000},
        "Honor": {"A": 150000, "B": 275000, "C": 480000}
    }

    
    status = status.capitalize()
    golongan = golongan.upper()

    if status not in gaji or golongan not in bonus[status]:
        print("Status atau golongan tidak valid!")
        return

    
    gaji_pokok = gaji[status]
    bonus_golongan = bonus[status][golongan]
    gaji_total = gaji_pokok + bonus_golongan

    
    print("\n=== Rincian Gaji ===")
    print(f"Nama       : {nama}")
    print(f"NIK        : {nik}")
    print(f"Status     : {status}")
    print(f"Golongan   : {golongan}")
    print(f"Gaji Pokok : Rp {gaji_pokok:,}")
    print(f"Bonus      : Rp {bonus_golongan:,}")
    print(f"Gaji Total : Rp {gaji_total:,}")


nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Tetap/Honor): ")
golongan = input("Masukkan Golongan (A/B/C): ")


hitung_gaji(nama, nik, status, golongan)
