
print('Tek kotek kotek kotek, anak ayam turun berkotek')
def ayam(n:int) :
    while True :
        if n <= 1 :
            print('anak ayam turunlah 1, mati satu tinggal induknya')
            break
        else:
            print(f'anak ayam turunlah {n}, mati satu tinggal {n -1}')

        n -= 1

if __name__ == '__main__':
    ayam(1)