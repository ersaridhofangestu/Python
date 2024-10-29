from contextlib import nullcontext

def create_matriks(n:int) -> list[int]:
    matriks:list = []  # Inisialisasi matriks kosong

    # Perulangan untuk setiap baris (i)
    for i in range(n):
        lines:list[int | nullcontext] = []  # Inisialisasi baris baru

        # Perulangan untuk setiap kolom (j) di dalam baris (i)
        for j in range(n):
            if j >= i:
                lines.append(j + 1)  # Isi dengan j + 1 jika j >= i
            else:
                lines.append(0)  # Isi dengan 0 jika j < i

        matriks.append(lines)  # Tambahkan baris ke dalam matriks

    return matriks

# Panggil fungsi dan cetak matriks
volume:int = 4  # Ukuran matriks (4x4)
result:list[int] = create_matriks(volume)

for line in result:
    print(line)
