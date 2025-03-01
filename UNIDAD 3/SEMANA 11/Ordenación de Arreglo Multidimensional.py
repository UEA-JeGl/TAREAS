# Programa 2: Ordenación de una fila en la matriz

def ordenar_fila(matriz, fila):
    matriz[fila].sort()
    return matriz

# Definir matriz 3x3
matriz_ordenacion = [
    [30, 10, 20],
    [60, 50, 40],
    [90, 70, 80]
]

fila_a_ordenar = 1
print("Matriz original:")
for fila in matriz_ordenacion:
    print(fila)

matriz_ordenada = ordenar_fila(matriz_ordenacion, fila_a_ordenar)
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)