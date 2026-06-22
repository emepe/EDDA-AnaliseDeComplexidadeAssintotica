def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

# Testes:
# lista ordenada
lista = [2, 5, 8, 10, 13, 21]

print(busca_binaria(lista, 2))    # caso 1: primeiro elemento
print(busca_binaria(lista, 10))   # caso 2: elemento no meio
print(busca_binaria(lista, 21))   # caso 3: último elemento
print(busca_binaria(lista, 7))    # caso 4: elemento que não existe
print(busca_binaria([], 3))       # caso 5: lista vazia

# Saída:
# -1
# -1
# -1
# -1
# None