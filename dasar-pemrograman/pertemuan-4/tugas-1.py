from inquirer import prompt, List, Text


class Karyawan:
    def __init__(self, gol, pen, jam):
        self.salary: float = 300000
        self.honor: float = 3500
        self.gol: float = gol
        self.pen: str = pen.lower()
        self.jam: float = jam

    def golongan(self) -> float:
        match self.gol:
            case 1:
                return self.salary * (5 / 100)
            case 2:
                return self.salary * (10 / 100)
            case 3:
                return self.salary * (15 / 100)
            case _:
                return 0

    def pendidikan(self) -> float:
        match self.pen:
            case "sma/smk":
                return self.salary * (0.5 / 100)
            case "d1":
                return self.salary * (5 / 100)
            case "d3":
                return self.salary * (20 / 100)
            case "s1":
                return self.salary * (30 / 100)
            case _:
                return 0

    def lembur(self) -> float:
        if self.jam == 9:
            return self.honor
        elif self.jam > 8:
            return self.honor * (self.jam - 8)
        else:
            return 0


if __name__ == "__main__":
    while True:
        questions = [
            Text('nama_karyawan', message='Masukkan Nama Karyawan? '),
            List('golongan',
                 message='Silakan pilih Golongan Jabatan? ',
                 choices=[1, 2, 3]),
            List('pendidikan',
                 message='Silakan pilih pendidikan? ',
                 choices=['SMA/SMK', 'D1', 'D3', 'S1']),
            Text('jam_kerja', message='Jumlah jam kerja? '),
        ]

        answers = prompt(questions)

        # Validasi nama karyawan
        if len(answers['nama_karyawan']) < 3:
            print("Untuk nama karyawan minimal 3 karakter.")
            continue  # Kembali untuk meminta input ulang

        # Validasi jam kerja
        jam_kerja = answers['jam_kerja']
        if not jam_kerja.isdigit():
            print("Untuk jam kerja anda hanya bisa mengisinya dengan digit/angka.")
            continue  # Kembali untuk meminta input ulang

        jam_kerja = int(jam_kerja)  # Jika valid, konversi ke integer

        # Buat instance Karyawan
        karyawan_instance = Karyawan(
            answers['golongan'],
            answers['pendidikan'],
            jam_kerja
        )

        # Hitung gaji
        golongan_salary = karyawan_instance.golongan()
        pendidikan_salary = karyawan_instance.pendidikan()
        lembur_salary = karyawan_instance.lembur()

        total_salary = karyawan_instance.salary + golongan_salary + pendidikan_salary + lembur_salary

        # Tampilkan hasil
        print(f'''
Karyawan yang bernama {str(answers['nama_karyawan']).capitalize()}
honor yang diterima
    Gaji Perbulan               Rp. {karyawan_instance.salary:,.0f}
    Tunjangan Jabatan           Rp. {golongan_salary:,.0f}
    Tunjangan Pendidikan        Rp. {pendidikan_salary:,.0f}
    Honor Lembur                Rp. {lembur_salary:,.0f}
                                --------------------- +
                                Rp. {total_salary:,.0f}
            ''')
        break  # Keluar dari loop jika semua input valid
