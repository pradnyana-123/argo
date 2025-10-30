import random

def show_board(hit, miss, comp, score):
    
    print("\n     Battleship Game")
    print(f"Sisa tebakan: {3 - len(miss)}")
    print(f"                        Score: {score}")    
    print("     0  1  2  3  4")

    place = 0
    huruf = ['A', 'B', 'C', 'D', 'E']
    for x in range(5):
        row = ""
        for y in range(5):
            ch = " _ "
            if place in miss:
                ch = " X "
            elif place in hit:
                ch = " O "
            elif place in comp:
                ch = " 0 "
            row += ch
            place += 1
        print(huruf[x], " ", row)

def get_shot(tebakan):
    while True:
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

            # Konversi ke posisi angka
            baris = ord(huruf) - 65
            kolom = int(angka)
            posisi = baris * 5 + kolom

            if posisi in tebakan:
                print("Sudah ditebak, coba posisi lain.")
            else:
                return posisi

        except:
            print("Input salah, coba lagi.")

def check_shot(shot, boat1, boat2, boat3, hit, miss, comp, score):

    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
            score += 2
        else:
            comp.append(shot)
            score += 3
            print("KAPAL 1 TENGGELAM!")
    elif shot in boat2:
        boat2.remove(shot)
        if len(boat2) > 0:
            hit.append(shot)
            score += 2
        else:
            comp.append(shot)
            score += 3
            print("KAPAL 2 TENGGELAM!")
    elif shot in boat3:
        boat3.remove(shot)
        if len(boat3) > 0:
            hit.append(shot)
            score += 2
        else:
            comp.append(shot)
            score += 3
            print("KAPAL 3 TENGGELAM!")
    else:
        miss.append(shot)
        score -= 1

    return boat1, boat2, boat3, hit, miss, comp

def tata_letak_boat():
    boats = []
    semua_posisi = set()
    for boat_length in [3, 3, 3]:
        while True:
            orientation = random.randint(0, 1)
            if orientation == 0:  # horizontal
                x = random.randint(0, 4)
                y = random.randint(0, 4 - boat_length + 1)
                positions = [x * 5 + (y + i) for i in range(boat_length)]
            else:  # vertical
                x = random.randint(0, 4 - boat_length + 1)
                y = random.randint(0, 4)
                positions = [(x + i) * 5 + y for i in range(boat_length)]
            if all(p not in semua_posisi for p in positions):
                boats.append(positions)
                semua_posisi.update(positions)
                break
    return boats[0], boats[1], boats[2]

# --- Game Loop Utama ---
def main():
    while True:
        hit = []
        miss = []
        comp = []
        score = 0
        boat1, boat2, boat3 = tata_letak_boat()

        for i in range(25):
            show_board(hit, miss, comp, score)
            tebakan = hit + miss + comp
            shot = get_shot(tebakan)
            boat1, boat2, boat3, hit, miss, comp = check_shot(
                 shot, boat1, boat2, boat3, hit, miss, comp, score
            )

        # Kondisi menang
            if len(boat1) == 0 and len(boat2) == 0 and len(boat3) == 0:
                print(f"Selamat, Anda menang!\nScore akhir: {score}")
                break

        # Kondisi kalah
            if len(miss) >= 3:
                print(f"Anda kalah.\nScore akhir: {score}")
                break

        ulang = input("Apakah Anda ingin mengulang game? (ya/no): ").lower()
        if ulang != "ya":
            print("Terima kasih sudah bermain!")
            break


if __name__ == "__main__":
    main()