from typing import List


def greatest(numbers: List[int]) -> int:
    # Jika hanya ada satu elemen, langsung kembalikan elemen tersebut
    if len(numbers) == 1:
        return numbers[0]

    # Rekursif untuk mencari nilai terbesar dari sisa elemen
    number_greatest = greatest(numbers[1:])

    # Kembalikan nilai terbesar antara elemen pertama dan hasil rekursif
    return numbers[0] if numbers[0] > number_greatest else number_greatest


if __name__ == '__main__':
    numbers: List[int] = [60, 20, 100, 40]

    # Cetak hasil fungsi greatest
    print(f"Nilai terbesar: {greatest(numbers)}")
