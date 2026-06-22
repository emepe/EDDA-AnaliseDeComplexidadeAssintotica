def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
   
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

# Testes:
print(merge_sort([5, 2, 9, 1, 3]))  # Saída: [1, 2, 3, 5, 9]

print(merge_sort([1, 2, 3, 4, 5]))  # Saída: [1, 2, 3, 4, 5]

print(merge_sort([4, 4, 2, 2, 1]))  # Saída: [1, 2, 2, 4, 4]

print(merge_sort([10]))             # Saída: [10]

print(merge_sort([]))               # Saída: []