# Matriz de 3 x 3
from types import new_class

matriz = [
    [5, 8, 3],
    [1, 7, 9],
    [2, 6, 4]
]

print(matriz)
# funcion buscar_valor especifico

def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor_buscado:
                return i,j

valor_buscado = 8
#print(buscar_valor(matriz,valor_buscado))


if valor_buscado == valor_buscado :
    print("Valor encontrado en la posicion ",buscar_valor(matriz,valor_buscado))
else:
    print("Valor invalido")















