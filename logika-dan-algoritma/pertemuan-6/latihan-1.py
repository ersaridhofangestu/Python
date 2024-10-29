def pangkat(x,y):
    if y == 0 :
        return 1
    else :
        return x * pangkat(x, y-1)

if __name__ == "__main__" :
    while True :
        try:
            x = int(input("Masukan Nilai X : "))
            y = int(input("Masukan Nilai Y : "))
            print(f"{x} dipangkatkan {y} = {pangkat(x,y)}")
            exit()
        except ValueError :
            print("Anda hanya bisa masukan type integer")