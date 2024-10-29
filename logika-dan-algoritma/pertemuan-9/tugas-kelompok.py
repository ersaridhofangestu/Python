def create_matriks(A, B):
    matriks = []  # Inisialisasi matriks kosong

    # Looping untuk setiap baris
    for i in range(len(A)):
        line = []  # Inisialisasi baris baru

        # Looping untuk setiap kolom
        for j in range(len(A[0])):
            line.append(A[i][j] + B[i][j])  # Tambahkan elemen yang bersesuaian

        matriks.append(line)  # Tambahkan baris ke matriks

    return matriks

# Inisialisasi matriks A dan B
matrik_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrik_B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Panggil fungsi dan simpan hasil penjumlahan
result = create_matriks(matrik_A, matrik_B)

# Cetak hasil penjumlahan
for line in result:
    print(line)
