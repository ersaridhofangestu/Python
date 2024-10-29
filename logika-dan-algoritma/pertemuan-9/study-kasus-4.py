nilai = [1, 2, 3, 4]  # Inisialisasi variabel dengan list

# Looping melalui setiap indeks dalam list 'nilai'
for i in range(len(nilai)):
    nilai[i] = 2 * i + 1  # Ganti nilai di indeks i dengan 2 * i + 1
    print(nilai[i])  # Cetak nilai yang baru

"""
    Algoritma:
        1. (Inisialisasi variabel) Membuat sebuah variabel bernama 'nilai' bertipe list dengan isi [1, 2, 3, 4].

        2. (Looping) Menggunakan perulangan berdasarkan range yang didapat dari panjang variabel 'nilai', yaitu 4, sehingga perulangan akan berlangsung sebanyak 4 kali. Nilai-nilai dari 0 hingga 3 akan disimpan dalam variabel 'i'.

        3. Di setiap iterasi perulangan:
            - Variabel 'i' akan digunakan sebagai indeks untuk mengakses elemen dalam list 'nilai'.
            - Pada setiap iterasi, elemen pada indeks 'i' di list 'nilai' akan diganti dengan hasil perhitungan `2 * i + 1`, yang akan menghasilkan nilai baru:
                - Untuk i = 0: `2 * 0 + 1` = 1
                - Untuk i = 1: `2 * 1 + 1` = 3
                - Untuk i = 2: `2 * 2 + 1` = 5
                - Untuk i = 3: `2 * 3 + 1` = 7

            - (Output) Setelah mengganti nilai, hasilnya akan dicetak menggunakan fungsi `print()`, sehingga setiap nilai yang baru akan ditampilkan satu per satu pada konsol.
                 1
                 3
                 5
                 7
"""
