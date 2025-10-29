import random

def show_board(hit, miss, comp):
    global score

    print("       Battleship Game", "\n")
    print("       0  1  2  3  4")
    print(f"score: {score}")

    place = 0
    huruf = ['A', 'B', 'C', 'D', 'E']
    for x in range(5):
        row = ""
        for y in range(5):
            ch = " _ "
            if place in miss:
                ch = " X "
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " O "
            row += ch
            place += 1
        print(huruf[x], " ", row)

def get_shot(tebakan):
    ok = "n"
    while ok == "n":
        try:
            shot = input("Masukkan tebakan anda (contoh: A1): ").upper().strip()
            if len(shot) < 2:
                print("Format salah! Gunakan huruf dan angka (contoh: A1).")
                continue

            huruf = shot[0]
            angka = shot[1]

            if huruf not in "ABCDE" or angka not in "01234":
                print("Koordinat tidak valid! Gunakan A-E dan 0-4.")
                continue

            # konversi ke posisi angka
            baris = ord(huruf) - 65
            kolom = int(angka)
            posisi = baris * 5 + kolom

            if posisi in tebakan:
                print("Sudah ditebak, coba posisi lain.")
            else:
                ok = "y"
                return posisi

        except:
            print("Input salah, coba lagi.")