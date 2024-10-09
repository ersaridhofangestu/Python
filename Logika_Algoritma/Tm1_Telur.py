from script.Format import Format 

Rupiah = Format()

HARGA_TELUR_PERKILO = 26_000  

berat_telur = 5

total_harga_telur = HARGA_TELUR_PERKILO * berat_telur

ongkos = 3_500 * 2
uang = 200_000

print(f'''
        berat telur {berat_telur} kg
        harga telur {Rupiah.ToMoney(HARGA_TELUR_PERKILO,'Rp.')}/kg
        transport {Rupiah.ToMoney(ongkos,'Rp.')}
        dan uang ibu {Rupiah.ToMoney(uang,'Rp.')}
      ''')

print(f'sisa uang ibu {Rupiah.ToMoney(uang - (total_harga_telur + ongkos), "Rp.")}')


# algoritma
    # Mulai program
    # 1. Deklarasikan HARGA_TELUR_PERKILO = 26.000
    # 2. Deklarasikan berat_telur = 5
    # 3. Hitung total_harga_telur = HARGA_TELUR_PERKILO * berat_telur

    # 4. Deklarasikan ongkos_sekali = 3.500
    # 5. Hitung ongkos = ongkos_sekali * 2

    # 6. Deklarasikan uang = 200.000

    # 7. Tampilkan:
    #    - berat telur
    #    - harga telur per kilogram yang diformat 
    #    - biaya transportasi yang diformat 
    #    - uang ibu yang diformat 

    # 8. Hitung sisa_uang = uang - (total_harga_telur + ongkos)

    # 9. Tampilkan sisa_uang

    # Selesai
