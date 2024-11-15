saldo = 50_000_000

def ambiluang(uang):
    if uang <= saldo:
        sisaSaldo = saldo - uang
        return print(f'''
Transaksi Berhasil
    saldo anda Rp. {saldo:,.0f}
    permintaan anda Rp {uang:,.0f}
    
    sisa saldo anda adalah {sisaSaldo:,.0f}
''')
    else:
        return print(f'''
Transaksi Gagal
    Saldo tidak cukup
''')

if __name__ == '__main__':
    uang = int(input("Masukan jumlah saldo yang ingin di tarik ? "))
    ambiluang(uang)