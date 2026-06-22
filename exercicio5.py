def imprimir_pares_e_soma(lista):
    # Bloco 1: imprime cada elemento
    for i in range(len(lista)):
        print(lista[i])

    # Bloco 2: imprime todos os pares
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i], lista[j])


# Testes:
lista1 = [1, 2, 3]
imprimir_pares_e_soma(lista1)

lista2 = [10]
imprimir_pares_e_soma(lista2)

lista3 = []
imprimir_pares_e_soma(lista3)

# Saídas:
# 1
# 2
# 3
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
# 10
# 10 10