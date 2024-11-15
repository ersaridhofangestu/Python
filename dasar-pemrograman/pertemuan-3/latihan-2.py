print("toko mainan anak".center(80," ").upper())
print(str("*"*40).center(80, " "))
name = input("Masukan Nama Pembeli ? ")
code = input("Masukan Kode Mainan ? ")
price = input("Masukan Harga ? ")
count = input("Masukan Jumlah Beli ? ")

print("="*80)
print(f'''
Nama Pembeli    =   {name.capitalize()}
kode Mainan     =   {code.upper()}
Harga           =   Rp. {int(price):,.0f}
Jumlah Beli     =   {str(count)} Pcs
Total           =   Rp. {int(price) * int(count):,.0f}
''')
