def create_matriks(n: int) -> list[list[int]]:
    matriks: list[list[int]] = []  # Inisialisasi matriks kosong

    # Perulangan untuk setiap baris (i)
    for i in range(n):
        lines: list[int] = []  # Inisialisasi baris baru

        # Perulangan untuk setiap kolom (j) di dalam baris (i)
        for j in range(n):
            if j <= i:
                lines.append(i + 1)  # Isi dengan i + 1 jika j <= i
            else:
                lines.append(0)  # Isi dengan 0 jika j > i

        matriks.append(lines)  # Tambahkan baris ke dalam matriks

    return matriks

# Panggil fungsi dan cetak matriks
volume: int = 4  # Ukuran matriks (4x4)
result: list[list[int]] = create_matriks(volume)

# Cetak setiap baris di matriks
for line in result:
    print(line)
