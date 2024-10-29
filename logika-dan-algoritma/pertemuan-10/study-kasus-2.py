def partition(arr):
    if not arr:  # Cek jika array kosong
        return arr, [], []

    pivot = arr[0]  # Ambil elemen pertama sebagai pivot
    pivot_arr = [pivot]  # Array yang hanya berisi pivot
    other_elements = []  # Array berisi elemen selain pivot

    print(f"Pivot: {pivot}")  # Tampilkan pivot

    # Iterasi mulai dari indeks ke-1 agar tidak termasuk pivot
    for x in arr[1:]:
        other_elements.append(x)  # Masukkan ke array elemen lainnya

    return arr, pivot_arr, other_elements

# Contoh penggunaan
array = [10, 15, 3 ,8 ,2 , 22]

# Memanggil fungsi dan menampilkan hasil
array1, array2, array3 = partition(array)

print("\nHasil Pembagian:")
print(f"Array 1 (Asli): {array1}")
print(f"Array 2 (Pivot): {array2}")
print(f"Array 3 (Selain Pivot): {array3}")
