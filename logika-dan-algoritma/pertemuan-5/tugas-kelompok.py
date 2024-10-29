def triangle(n, symbol, current=1):
    # Basis Case: Jika baris saat ini lebih besar dari n, hentikan rekursi
    if current > n:
        return

    # Cetak baris dengan spasi dan symbol
    print(' ' * (n - current) + f'{symbol} ' * current)

    # Panggil fungsi rekursif untuk mencetak baris berikutnya
    triangle(n, symbol, current + 1)

if __name__ == "__main__" :

    while True :
        symbol = input("Masukan simbol : ")
        try:
            hight = int(input("Masukan tinggi bangunan : "))
            triangle(hight, symbol)
            exit()
        except ValueError:
            print("Anda hanya bisa memasukan type data integer")

