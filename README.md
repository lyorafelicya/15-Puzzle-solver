# Tugas Kecil 3 IF2211 Strategi Algoritma - 15 Puzzle Solver
Merupakan sebuah program untuk menyelesaikan persoalan 15-Puzzle dengan memanfaatkan Algoritma Branch and Bound. 15-Puzzle merupakan sebuah permainan puzzle berukuran 4x4 dengan 15 kotaknya berisi ubin bernomor 1-15, serta terdapat satu buah kotak kosong untuk melakukan pergeseran. Ubin dapat 
digerakkan ke atas, bawah, kiri, dan kanan. Tujuan akhir pada permainan ini adalah untuk mengurutkan ubin dari nomor 1 hingga 15 secara berurutan dan menyisakan ubin kosong di kotak terakhir. Program memiliki 2 metode input persoalan, yaitu dengan file txt yang berisi puzzle yang ingin diselesaikan ataupun puzzle dibangkitkan secara acak oleh program. Program ini dibuat dalam bahasa python.

## Requirement Program
1. Python

## Cara menggunakan Program
1. Buka terminal pada direktori folder src
2. Jalankan file yang bernama main.py dengan menuliskan perintah ```python main.py``` pada terminal
3. Pilih metode input puzzle yang diinginkan
4. Jika memilih input file, tuliskan nama file dari puzzle yang ingin diselesaikan, dengan .txt (perhatikan bahwa lokasi file harus berada di dalam folder test).
5. Tekan enter dan program akan mulai melakukan pencarian solusi.

## Output program
1. Matriks posisi awal 15-Puzzle
2. Nilai dari fungsi Kurang(i) untuk setiap ubin
3. Nilai dari Kurang(i) + X
4. Pesan apabila puzzle tidak dapat diselesaikan
5. Path aksi yang dilakukan dari posisi awal ke susunan akhir
6. Waktu eksekusi program
7. Jumlah simpul yang dibangkitkan selama pencarian

## Format File txt
Program dapat menerima input berupa nama file teks yang berisi matriks puzzle berukuran 4x4 yang terdiri atas angka 0 - 15 (antar angka dipisahkan oleh spasi). Angka 0 digunakan sebagai penanda ubin kosong.
Berikut adalah contoh isi file teks yang benar
```
5 1 3 4
9 2 7 8
0 6 15 11
13 10 14 12
```

## Author
> Lyora Felicya - 13520073
