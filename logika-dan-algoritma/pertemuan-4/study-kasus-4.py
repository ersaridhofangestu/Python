from script import to_money

try:
    sum_products = int(input("Masukan jumlah banyaknya produk yang terjual: "))
    price_product = int(input("Masukan harga satuan produk: "))

    basic_salary = 5_000_000 # Gaji pokok
    min_sales = 100  # Minimal penjualan untuk bonus
    sales = 10  # Bonus 10%

    # Hitung total penjualan
    total_sales = sum_products * price_product

    # Hitung bonus jika penjualan di atas 100 produk
    if sum_products >= min_sales:
        total_sales = (sales / 100) * total_sales
    else:
        total_sales = 0

    # Hitung total gaji
    total_gaji = basic_salary + total_sales

    # Cetak hasil
    print(f"Total penjualan: {to_money(total_sales, 'Rp')}")
    print(f"Bonus: {to_money(total_sales, 'Rp')}")
    print(f"Total gaji: {to_money(total_gaji, 'Rp')}")

except ValueError :
    print("Input tidak valid. Harap masukkan angka.")
