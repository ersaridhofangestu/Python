def tampilkan_kotak(arr):
    """Fungsi untuk menampilkan elemen dalam format kotak."""
    print("\n+-------+")
    for number in arr:
        print(f"| {number:^5} |")  # Menampilkan angka di tengah kotak
    print("+-------+")


def main():
    nilai = [25, 20, 15, 3, 7, 2, 1]

    print("Daftar Nilai:")
    print("-------------------------")
    print(nilai)
    print("-------------------------")

    nilai_tengah = len(nilai) // 2

    # Pembagian proses
    proses_a = nilai[:nilai_tengah]
    proses_b = nilai[nilai_tengah:]

    print("\nProses Pembagian:")
    print(f"Proses A: {proses_a}")
    print(f"Proses B: {proses_b}")
    print("-------------------------")

    # Menampilkan setiap elemen dalam kotak
    print("Elemen Proses A dalam Kotak:")
    tampilkan_kotak(proses_a)

    print("Elemen Proses B dalam Kotak:")
    tampilkan_kotak(proses_b)

    # Proses menghitung max dan min
    max_a = max(proses_a)
    min_a = min(proses_a)
    max_b = max(proses_b)
    min_b = min(proses_b)

    print("\nHasil Conquer:")
    print(f"Max Proses A: {max_a}, Min Proses A: {min_a}")
    print(f"Max Proses B: {max_b}, Min Proses B: {min_b}")
    print("-------------------------")

    # Menampilkan hasil akhir
    print("Hasil Akhir:")
    print(f"Nilai: {nilai},\nMax: {max(nilai)},\nMin: {min(nilai)}")
    print("-------------------------")


# Menjalankan fungsi main

if __name__ == "__main__" :
    main()

