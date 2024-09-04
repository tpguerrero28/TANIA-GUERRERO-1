#ejercicio 2 matriz 3 x 3
matriz = [
    [5, 8, 3],
    [1, 7, 9],
    [2, 6, 4]
]

# Función para ordenar una fila específica usando Bubble Sort
def bubble_sort_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila que queremos ordenar (por ejemplo, la fila 1)
fila_a_ordenar = 1

# Ordenamos la fila específica
bubble_sort_fila(matriz, fila_a_ordenar)

# Mostramos la matriz después de ordenar la fila
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
