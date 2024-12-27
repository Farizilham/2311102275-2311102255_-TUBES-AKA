import numpy as np
import time
from bisect import bisect_left

# Fungsi pencarian linear
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Fungsi pencarian biner
def binary_search(arr, target):
    index = bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    return -1

# Fungsi untuk menghitung determinan dengan metode kofaktor
def determinant_cofactor(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(size):
        sub_matrix = np.delete(np.delete(matrix, 0, axis=0), col, axis=1)
        det += ((-1) ** col) * matrix[0][col] * determinant_cofactor(sub_matrix)
    return det

# Fungsi untuk menghitung determinan dengan metode elementer
def determinant_elementary(matrix):
    size = len(matrix)
    mat = np.array(matrix, dtype=float)
    det = 1

    for i in range(size):
        if mat[i][i] == 0:
            for j in range(i + 1, size):
                if mat[j][i] != 0:
                    mat[[i, j]] = mat[[j, i]]
                    det *= -1
                    break
        
        if mat[i][i] == 0:
            return 0

        det *= mat[i][i]
        mat[i] = mat[i] / mat[i][i]

        for j in range(i + 1, size):
            mat[j] -= mat[i] * mat[j][i]

    return det

# Fungsi untuk mengukur waktu eksekusi
def measure_execution_time(method, search_method, matrix, target):
    start_time = time.perf_counter()

    if search_method == "linear":
        linear_search(matrix.flatten(), target)
    elif search_method == "binary":
        sorted_matrix = np.sort(matrix.flatten())
        binary_search(sorted_matrix, target)

    if method == "cofactor":
        determinant = determinant_cofactor(matrix)
    elif method == "elementary":
        determinant = determinant_elementary(matrix)

    end_time = time.perf_counter()
    return end_time - start_time, determinant

# Eksperimen utama
methods = ["cofactor", "elementary"]
search_methods = ["linear", "binary"]

matrices = {
    "4x4": np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]),
    "5x5": np.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25]]),
    "6x6": np.array([[1, 2, 3, 4, 5, 6],
                     [7, 8, 9, 10, 11, 12],
                     [13, 14, 15, 16, 17, 18],
                     [19, 20, 21, 22, 23, 24],
                     [25, 26, 27, 28, 29, 30],
                     [31, 32, 33, 34, 35, 36]])
}

target = 1  # Elemen yang dicari secara langsung

for label, matrix in matrices.items():
    size = len(matrix)
    print(f"\nUkuran Matriks: {label}")
    print("Matriks:")
    print(matrix)
    for method in methods:
        for search_method in search_methods:
            time_taken, determinant = measure_execution_time(method, search_method, matrix, target)
            print(f"Metode: {method}, Determinan: {determinant}, Pencarian: {search_method}, Waktu: {time_taken:.6f} detik")