from script import to_money

# Deklarasi variabel
berat_telur: int = 5  # Jumlah telur yang dibeli ibu
harga_telur: int = 26_000  # Harga telur per kilogram
ongkos: int = 3_500 * 2  # Ongkos pulang pergi
uang_ibu: int = 200_000  # Total uang ibu

# Perhitungan total harga telur
total_harga_telur: int = harga_telur * berat_telur

# Menghitung sisa uang ibu
total_pengeluaran: int = total_harga_telur + ongkos
sisa_uang: int = uang_ibu - total_pengeluaran

# Output menggunakan fungsi to_money
print(f'''
Berat telur: {berat_telur} kg
Harga telur: {to_money(harga_telur, "Rp")}/kg
Total harga telur: {to_money(total_harga_telur, "Rp")}
Transport: {to_money(ongkos, "Rp")}
Uang ibu: {to_money(uang_ibu, "Rp")}

Sisa uang ibu adalah: {to_money(sisa_uang, "Rp")}
''')
