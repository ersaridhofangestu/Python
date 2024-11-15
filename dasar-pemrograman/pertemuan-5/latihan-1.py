pesanan = []

print("gerobak fried chicken".upper())
print(f'''
{"-"*30}
kode    jenis-potongan    harga
{"-"*30}
 D           Dada        Rp. 2500
 P           Paha        Rp. 2000
 S           Sayap       Rp. 1500
{"-"*30}



''')

no = 1

while True:
    code: str = input("Kode Potongan [D/P/S] ? ")
    jumlah: int = int(input("Jumlah ? "))
    lanjut: str = input("Apakah anda ingin memilih lagi [y/n] ? ")

    match code.upper() :
        case "D" :
            jenis_potongan = "Dada"
            harga_satuan = 2500
        case "P" :
            jenis_potongan = "Paha"
            harga_satuan = 2500
        case "S" :
            jenis_potongan = "Sayap"
            harga_satuan = 2500
            print(harga_satuan)
        case _:
            harga_satuan = 0
            jenis_potongan = None
            print("anda hanya bisa memilih [D/P/S].")


    data = {
        "no": no,
        "jenis-potongan": jenis_potongan,
        "jumlah": jumlah,
        "harga": harga_satuan,
        "total-harga": harga_satuan * jumlah
    }

    pesanan.append(data)

    if lanjut.upper() == "Y" :
        no += 1
        continue
    if lanjut.upper() == "N" :
        no += 1
        break
    else:
        print("anda hanya bisa mengisi y atau n")
        break

print(f'''
{"gerobak fried chicken".upper()}
{"-"*50}
No.  jenis      Harga           Banyak      Jumlah
    Potongan   Satuan           Beli        Harga
{"-"*50}''')

total_harga = 0

for pesan in pesanan:
    print(f'''
{pesan["no"]}   {pesan["jenis-potongan"]}       Rp. {int(pesan["harga"]):,.0f}      {pesan["jumlah"]} pcs       Rp. {int(pesan["total-harga"]):,.0f}
    ''',end=" ")
    total_harga += pesan["total-harga"]

print(f'''
{"-"*50}

                        jumlah banyak   Rp. {total_harga:,.0f}
                        pajak 10%       Rp. {total_harga - (total_harga / 10):,.0f}
                        total bayar     Rp. {total_harga + (total_harga - (total_harga / 10)):,.0f}
''')

