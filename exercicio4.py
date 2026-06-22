def pares_com_soma(lista, alvo):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                print(lista[i], lista[j])

# Testes:
lista1 = [1, 2, 3, 4, 5]
pares_com_soma(lista1, 6)   # Saída: (1,5), (2,4)

lista2 = [10, 7, 3, 8]
pares_com_soma(lista2, 17)  # Saída: (10,7)

lista3 = [1, 1, 1]
pares_com_soma(lista3, 10)  # Saída: não imprime nada

lista4 = [2, 4]
pares_com_soma(lista4, 6)   # Saída: (2,4)

lista5 = []
pares_com_soma(lista5, 5)   # Saída: não imprime nada