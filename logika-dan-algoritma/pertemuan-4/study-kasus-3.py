from script import to_money

tarif_awal = 6000  # tarif per jam awal
tarif_berikutnya = 5000  # tarif per jam berikutnya
sewa = 3  # sewa selama 3 jam

# Menghitung total tarif berdasarkan durasi sewa
if sewa > 1:
    sewa -= 1  # Mengurangi 1 jam karena jam pertama sudah terhitung
    total_tarif = tarif_awal + (tarif_berikutnya * sewa)  # Tarif jam pertama + tarif jam berikutnya
else:
    total_tarif = tarif_awal  # Hanya tarif jam pertama jika sewa 1 jam atau kurang

print(f'Total tarif sewa: {to_money(total_tarif,"Rp")}')  # Menampilkan total tarif
