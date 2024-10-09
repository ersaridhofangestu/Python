from script.Format import Format

Rupiah = Format()

harga = int(input('Masukan harga mangga/kg ? '))
berat = int(input('Masukan berat pembelian | kg ? '))

total = harga * berat

print(f'Harga yang dibayarkan pembeli adalah {Rupiah.ToMoney(total,'Rp.')}')

# Algoritma:
    # Mulai program
    # 1. Minta input harga mangga per kilogram dari pengguna dan konversi ke integer
    # 2. Minta input berat pembelian dalam kilogram dari pengguna dan konversi ke integer
    # 3. Hitung total harga dengan mengalikan harga per kilogram dengan berat pembelian
    # 4. Tampilkan total harga yang dibayarkan pembeli
    # Program selsai
    