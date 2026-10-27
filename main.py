import time

def tampilkan_header():
    print("=" * 40)
    print("            CAMPUSQUEST")
    print("      Student Productivity Quest")
    print("=" * 40)

total_xp = 0
total_menit = 0
jumlah_quest_selesai = 0

tampilkan_header()
nama = input("Masukkan nama: ")
if not nama:
    print("Nama tidak boleh kosong.")

fakultas = input("Masukkan fakultas: ")
print ("Selamat datang",nama, "dari", fakultas)

pilihan_durasi = [30, 60, 90, 120]

def pilih_durasi():
    for i, durasi in enumerate(pilihan_durasi, start=1):
        print(f"{i}. {durasi} menit")

    pilihan = input("Pilih durasi (1-4): ")

    if pilihan in ["1", "2", "3", "4"]:
        return pilihan_durasi[int(pilihan) - 1]
    else:
        print("Pilihan tidak valid.")
        return None

def jalankan_timer(durasi_menit):
    durasi_detik = int(durasi_menit)

    print("\nTimer dimulai!")
    waktu_mulai = time.monotonic()

    while True:
        waktu_berlalu = time.monotonic() - waktu_mulai
        sisa_waktu = durasi_detik - waktu_berlalu

        if sisa_waktu <= 0:
            break

        menit = int(sisa_waktu // 60)
        detik = int(sisa_waktu % 60)

        print(f"Sisa waktu: {menit:02d}:{detik:02d}", end="\r", flush=True)
        time.sleep(1)

    print("\nWaktu belajar selesai!")




while True:
    print("\n" + "-" * 40)
    aktivitas = input("Kamu mau belajar apa? (ketik 'selesai' untuk keluar): ")

    if aktivitas == "selesai":
        break
    if not aktivitas:
        print("Aktivitas tidak boleh kosong.")
        

    print("Aktivitas kamu",aktivitas)
    durasi_menit = pilih_durasi()
    if durasi_menit is None:
        continue
    print("Target belajar",durasi_menit, "menit")
    jalankan_timer(durasi_menit*60)

    print("Waktunya istirahat!")
    print("1. Istirahat 5 menit")
    print("2. Istirahat 10 menit")
    pilihan_istirahat = input("Pilih istirahat (1/2): ")

    if pilihan_istirahat == "1":
        durasi_istirahat = 5
    elif pilihan_istirahat == "2":
        durasi_istirahat = 10
    else:
        print("Pilihan tidak valid, otomatis 5 menit.")
        durasi_istirahat = 5

    sisa_waktu = durasi_istirahat * 60
    while sisa_waktu > 0:
        menit = sisa_waktu // 60
        detik = sisa_waktu % 60
        print(f"Sisa istirahat: {menit:02d}:{detik:02d}", end="\r", flush=True)
        time.sleep(1)
        sisa_waktu -= 1

    print("Istirahat selesai!")


    selesai = input("Apakah aktivitas selesai? (ya/tidak): ")

    if selesai == "ya":
        xp = (durasi_menit // 10) * 10
        total_xp += xp
        total_menit += durasi_menit
        jumlah_quest_selesai += 1
    else:
        xp = 0


print("\n===== RINGKASAN BELAJAR =====")
print(nama,"Fakultas:", fakultas)
print("Quest selesai:", jumlah_quest_selesai)
print("Total waktu belajar:", total_menit, "menit")
print("Total XP:", total_xp)


print("\nTerima kasih sudah menggunakan CampusQuest!")