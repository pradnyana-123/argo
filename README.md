### Battleship Game (Python Console)

Program ini adalah permainan Battleship sederhana berbasis teks menggunakan bahasa Python.
Tujuan permainan ini adalah menebak lokasi kapal musuh yang tersembunyi di papan berukuran 5x5.

============================================================
### Deskripsi Singkat

Terdapat tiga kapal di papan permainan, masing-masing berukuran tiga kotak.
Kapal-kapal tersebut diletakkan secara acak, baik horizontal maupun vertikal.
Pemain diberi kesempatan untuk menebak posisi kapal dengan cara memasukkan koordinat seperti A1, B3, dan sebagainya.

============================================================

### Cara Bermain

- Saat permainan dimulai, kamu memiliki 3 kesempatan meleset.

- Masukkan tebakan dengan format satu huruf dan satu angka, misalnya B2.

- Huruf menunjukkan baris (A–E).

- Angka menunjukkan kolom (0–4).

- Jika tebakanmu mengenai kapal, kamu akan mendapatkan +2 poin.

- Jika dengan tebakan itu kapal tenggelam sepenuhnya, kamu akan mendapatkan tambahan +3 poin.

- Jika tebakanmu salah, maka kamu kehilangan 1 poin, dan kesempatan melesetmu berkurang satu.

- Permainan berakhir jika:

- Semua kapal berhasil kamu tenggelamkan (menang), atau

- Kamu sudah 3 kali menembak meleset (kalah).

- Setelah permainan selesai, kamu dapat memilih untuk mengulang permainan atau keluar.

 ============================================================  
### Sistem Skor

Mengenai kapal: +2 poin  
Menenggelamkan kapal: +3 poin  
Meleset: -1 poin

============================================================

# Fungsi Utama Program

show_board()  
→ Menampilkan papan permainan, skor, dan sisa kesempatan menebak.

get_shot()  
→ Menerima input tebakan dari pemain dan memastikan formatnya benar.

check_shot()  
→ Mengevaluasi hasil tebakan dan memperbarui skor serta status kapal.

tata_letak_boat()  
→ Menentukan posisi tiga kapal di papan secara acak tanpa bertabrakan.

