# ⚓ Permainan Battleship (Kapal Perang)

Ini adalah implementasi sederhana dari permainan klasik **Battleship** menggunakan Python. Tujuannya adalah menenggelamkan semua kapal musuh dalam jumlah tebakan yang terbatas.

---

## 🎯 Cara Bermain

1.  **Jalankan Kode:** Pastikan Anda memiliki interpreter Python terinstal. Simpan kode di atas sebagai file Python (misalnya `battleship.py`) dan jalankan dari terminal:
    ```bash
    python battleship.py
    ```

2.  **Papan Permainan:** Papan permainan berukuran $5 \times 5$ dengan baris berlabel **A** hingga **E** dan kolom berlabel **0** hingga **4**.

    ```
      0  1  2  3  4
    A  _  _  _  _  _
    B  _  _  _  _  _
    C  _  _  _  _  _
    D  _  _  _  _  _
    E  _  _  _  _  _
    ```

3.  **Kapal:** Ada **3 kapal** yang masing-masing memiliki panjang **3 petak** (blok). Letak kapal diacak pada setiap permainan baru.

4.  **Tebakan:** Masukkan tebakan Anda dalam format **HurufAngka** (contoh: `A1`, `B3`, `E4`).

5.  **Simbol:**
    * **$\_$**: Petak yang belum ditebak.
    * **X**: **Miss** (Tebakan meleset).
    * **O**: **Hit** (Tebakan kena kapal, tetapi kapal belum tenggelam).
    * **0**: **Comp** (Kapal **Tenggelam/Tenggelam Total**).

---

## 🏆 Aturan Skor

Sistem skor diterapkan untuk menambah tantangan:

| Aksi | Perubahan Skor | Keterangan |
| :--- | :--- | :--- |
| **Kena (Hit)** | **+2** | Tebakan mengenai kapal, kapal belum tenggelam. |
| **Tenggelam (Comp)** | **+3** | Tebakan terakhir yang menenggelamkan kapal. |
| **Meleset (Miss)** | **-1** | Tebakan tidak mengenai kapal mana pun. |

---

## ❗ Kondisi Menang/Kalah

| Kondisi | Hasil |
| :--- | :--- |
| **Menang** | Semua kapal $(3 \times 3 \text{ petak})$ telah berhasil ditenggelamkan. |
| **Kalah** | Anda membuat **3 kali** tebakan **meleset (Miss)**. |

---

## 🛠️ Detail Teknis

### Fungsi-fungsi Utama

| Fungsi | Deskripsi |
| :--- | :--- |
| `show_board` | Menampilkan papan permainan saat ini beserta *score* dan sisa tebakan. |
| `get_shot` | Meminta input tebakan dari pemain, melakukan validasi, dan mengonversinya ke posisi angka (`0-24`). |
| `check_shot` | Memeriksa apakah tebakan mengenai kapal, mencatat hasilnya (**hit**, **miss**, atau **comp**), dan menyesuaikan *score*. |
| `tata_letak_boat` | Mengacak posisi 3 kapal berukuran 3 petak di papan, memastikan tidak ada kapal yang tumpang tindih. |

### Variabel Global

* `score`: Menyimpan skor permainan saat ini (diakses dan diubah oleh `show_board` dan `check_shot`).

---

## ✍️ Kontributor

* *(Ganti dengan nama/alias Anda)*
