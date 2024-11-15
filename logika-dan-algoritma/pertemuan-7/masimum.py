def maxmimum(n) :
    if len(n) == 1 :
        return n[0]

    nilaiMax = maxmimum(n[1:])

    return n[0] if n[0] > nilaiMax else nilaiMax

def minmimum(n) :
    if len(n) == 1 :
        return n[0]

    nilaiMax = maxmimum(n[1:])

    return n[0] if n[0] < nilaiMax else nilaiMax

if __name__ == '__main__':
    array = [10,30,50,70,100]
    NilaiMax, NilaiMin = maxmimum(array), minmimum(array)
    print(f'''
array = {array}
nilai terbesar dari {array} adalah {NilaiMax}
nilai terkecil dari {array} adalah {NilaiMin}
''')

