def faktorial(n):
    if n < 1 :
        return 1
    
    return n * faktorial(n-1)

if __name__ == "__main__" :
    while True :
        try :
            nilai = int(input("Masukan Nilai faktorial : "))
            hasil = faktorial(5)
            print(f'{nilai}! = {hasil}')
            exit()
        except ValueError :
            print("Anda hanya bisa memasukan type integer")