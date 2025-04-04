def determinante( matriz):

    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    det = 0
    for columna in range(len(matriz[0])):
        matriz2 = [fila[:columna] + fila[columna + 1:] for fila in matriz[1:]]
        det += ((-1) ** columna) * matriz[0][columna] * determinante(matriz2)

    return det

print(determinante([
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]))