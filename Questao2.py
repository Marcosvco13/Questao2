def contar_submatriz(matriz_a, submatriz_b):
    count = 0
    rows_a, cols_a = len(matriz_a), len(matriz_a[0])
    rows_b, cols_b = len(submatriz_b), len(submatriz_b[0])

    for i in range(rows_a - rows_b + 1):
        for j in range(cols_a - cols_b + 1):
            if verifica_submatriz(matriz_a, submatriz_b, i, j):
                count += 1

    return count

def verifica_submatriz(matriz_a, submatriz_b, start_row, start_col):
    rows_b, cols_b = len(submatriz_b), len(submatriz_b[0])

    for i in range(rows_b):
        for j in range(cols_b):
            if matriz_a[start_row + i][start_col + j] != submatriz_b[i][j]:
                return False

    return True

# Exemplo de uso
matriz_a = [
    [1, 2, 3, 4],
    [5, 2, 1, 4],
    [2, 3, 4, 1],
    [1, 2, 3, 4]
]

submatriz_b = [
    [2, 1],
    [3, 4]
]

resultado = contar_submatriz(matriz_a, submatriz_b)
print(f"A submatriz B pode ser encontrada {resultado} vezes na matriz A.")
