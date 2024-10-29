def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
if __name__ == "__main__" :
    while True :
        try :
            x = int(input("Masukan batasan deret bilangan fibonacci : "))
            print("Deret fibonacci")
            for i in range(x):
                print(fibonacci(i), end=" ")
            exit()
        except ValueError :
            print("Anda hanya memasukan integer")