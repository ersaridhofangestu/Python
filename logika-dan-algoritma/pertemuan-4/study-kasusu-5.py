from script import to_money

# Input
gaji_pokok = int(input("Masukan gaji pokok karyawan: "))
jam_kerja = int(input("Masukan jumlah jam kerja: "))

# Konstanta dan perhitungan dasar
lembur_per_jam = 20_000
tunjangan = (20 / 100) * gaji_pokok
pajak = (10 / 100) * gaji_pokok
gaji_tambahan = tunjangan

# Hitung uang lembur jika ada
if jam_kerja > 200:
    jam_lembur = jam_kerja - 200
    uang_lembur = jam_lembur * lembur_per_jam
    gaji_tambahan += uang_lembur
else:
    jam_lembur = 0
    uang_lembur = 0

# Hitung gaji bersih
gaji_bersih = gaji_pokok - pajak + gaji_tambahan

# Output
print(f'''
Gaji pokok: {to_money(gaji_pokok, "Rp")}
Jam kerja: {jam_kerja} jam dan max jam kerja 200
Jam lembur: {jam_lembur} jam x 20.000
Uang lembur: {to_money(uang_lembur, "Rp")}
Tunjangan: {to_money(tunjangan, "Rp")}
Pajak: {to_money(pajak, "Rp")}
Total Gaji Bersih: {to_money(gaji_bersih, "Rp")}
''')

print(f"Gaji bersih: {to_money(gaji_bersih, 'Rp')}")
