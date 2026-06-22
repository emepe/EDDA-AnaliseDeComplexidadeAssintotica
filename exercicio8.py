def ordenacao_bolha(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Teste:
print(ordenacao_bolha([1, 2, 3, 4, 5]))     # Saída: [1, 2, 3, 4, 5]

print(ordenacao_bolha([5, 4, 3, 2, 1]))     # Saída: [1, 2, 3, 4, 5]

print(ordenacao_bolha([3, 1, 2, 3, 1]))     # Saída: [1, 1, 2, 3, 3]

print(ordenacao_bolha([10]))                # Saída: [10]

print(ordenacao_bolha([]))                  # Saída: []

