import math

def Latihan1():
    try :
        gross = input('Masukan nilai Gros ? ')
        buah = int(gross) * 144
        return print(f'Nilai buah adalah {buah}')
    except ValueError:
        return print('Anda harus memasukan angka bukan huruf')
        
    # Algoritma:
        # 1. Minta input nilai Gros dari pengguna.
        # 2. Gunakan try-except untuk menangani kesalahan input yang tidak valid.
        # 3. Jika input valid, hitung nilai buah dengan mengalikan nilai Gros dengan 144.
        # 4. Tampilkan nilai buah ke layar.
    

def Latihan2():
    try :
        r = input('Masukan nilai r ? ')
        kell = 2 * math.pi * int(r)    
        return print(f'Nilai kel adalah {kell}')
    except ValueError :
        return print('Anda harus memasukan angka bukan huruf')
        
    # Algoritma:
        # 1. Impor modul math untuk akses konstanta pi.
        # 2. Definisikan fungsi Latihan2.
        # 3. Minta input nilai jari-jari dari pengguna dan simpan dalam variabel r.
        # 4. Hitung keliling lingkaran menggunakan rumus 2 * phi * r.
        # 5. Tampilkan hasil keliling ke layar.


def Latihan3():
    try :
        Bilangan = 0
        while Bilangan < 12:
            print(Bilangan)
            Bilangan += 4
    except ValueError:
        return print('Anda harus memasukan angka bukan huruf')

    # Algoritma:
        # 1. Inisialisasi variabel Bilangan dengan nilai 0.
        # 2. Mulai loop while selama Bilangan kurang dari 12.
        #    a. Cetak nilai Bilangan.
        #    b. Tambahkan 4 ke variabel Bilangan.
        # 3. Panggil fungsi Latihan3 untuk menjalankan program.
        

def Latihan4():
    try:
        Nilai = input('Masukan nilai ? ')
        if int(Nilai) > 70:
            return print(f'Anda lulus dengan nilai {Nilai}')
        else:
            return print(f'Anda Her')
    except ValueError :
        return print('Anda harus memasukan angka bukan huruf')
    
    # Algoritma:
        # 1. Minta input nilai dari pengguna.
        # 2. Gunakan try-except untuk menangani kesalahan input yang tidak valid.
        # 3. Jika input valid, periksa apakah nilainya lebih dari 70.
        # 4. Tampilkan pesan lulus atau tidak lulus berdasarkan nilai.

def Latihan5():
    try : 
        bil = 1
        for bil in range(1,10):
            print(bil)
            bil += 1
    except ValueError:
        return print('Anda harus memasukan angka bukan huruf')
        
    # Algoritma:
        # 1. Inisialisasi variabel bil dengan nilai 1.
        # 2. Gunakan loop for untuk iterasi bil dari 1 hingga 9 menggunakan range(1, 10).
        # 3. Dalam setiap iterasi, lakukan langkah berikut:
        #    a. Cetak nilai bil.
        # 4. Selesai.
                