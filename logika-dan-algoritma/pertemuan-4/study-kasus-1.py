import inquirer
from typing import List

questions: List[object] = [
    inquirer.List('options',
                  message="Silakan pilih nilai variable A dan B",
                  choices=[
                      'A. 4 dan 6',
                      'B. 3 dan 5',
                      'C. 9 dan 6',
                      'exit'
                  ]
    )
]

try:
    # Ambil pilihan dari prompt
    option = inquirer.prompt(questions)['options']

    # Definisikan a dan b
    a: int = 0
    b: int = 0

    # Menggunakan match-case untuk menentukan nilai a dan b
    match option:
        case 'A. 4 dan 6':
            a += 4
            b += 6
        case 'B. 3 dan 5':
            a += 3
            b += 5
        case 'C. 9 dan 6':
            a += 9
            b += 6
        case 'exit':
            print("Program dihentikan.")
            exit()

    # Menghitung nilai c dan d
    if a > b:
        c = a + b
    else:
        c = b + a
    d = c * c

    # Menampilkan hasil
    print(f'''
variable a adalah {a}
variable b adalah {b}
variable c adalah {c}
variable d adalah {d}
''')

except ValueError:
    print("Server error")
