try:
    # Input harga telur per kilogram (dalam bentuk integer)
    harga_telur = int(input("Masukkan harga telur per kg: "))

    # Input berat telur yang dibeli (dalam bentuk integer)
    berat_telur = int(input("Masukkan berat telur (kg): "))

    # Menghitung total harga dengan mengalikan harga per kg dengan berat
    total_harga = harga_telur * berat_telur

    # Menampilkan total harga yang harus dibayar
    print(f'Harga yang harus dibayar: {total_harga}')

# Jika terjadi kesalahan saat memasukkan input (bukan angka), tangkap dengan exception ini
except ValueError:
    # Pesan error ketika pengguna memasukkan huruf atau karakter yang tidak valid sebagai angka
    print("Saya harap Anda memasukkan angka, bukan huruf.")
