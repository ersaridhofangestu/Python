def create_matriks(n: int) -> list[list[int]]:
    matriks: list[list[int]] = []  # Inisialisasi matriks kosong

    # Perulangan untuk setiap baris (i)
    for i in range(n):
        line: list[int] = []  # Inisialisasi baris baru

        # Perulangan untuk setiap kolom (j) di dalam baris (i)
        for j in range(n):
            if j == i:
                line.append(1)  # Isi diagonal dengan 1
            else:
                line.append(0)  # Isi non-diagonal dengan 0

        matriks.append(line)  # Tambahkan baris ke dalam matriks

    return matriks

# Panggil fungsi dan cetak matriks
volume: int = 4  # Ukuran matriks (4x4)
result: list[list[int]] = create_matriks(volume)

# Cetak setiap baris di matriks
for line in result:
    print(line)
