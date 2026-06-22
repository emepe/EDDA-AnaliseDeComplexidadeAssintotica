def produto_de_matrizes(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Testes:
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print("Teste 1:")
C = produto_de_matrizes(A, B, 2)
print(C)  # esperado: [[19, 22], [43, 50]]

# Teste 2: identidade 2x2
I = [[1, 0],
     [0, 1]]

print("Teste 2:")
C2 = produto_de_matrizes(A, I, 2)
print(C2)  # esperado: igual a A -> [[1,2],[3,4]]

# Teste 3: matriz 1x1
A1 = [[2]]
B1 = [[3]]
print("Teste 3:")
print(produto_de_matrizes(A1, B1, 1))  # esperado: [[6]]