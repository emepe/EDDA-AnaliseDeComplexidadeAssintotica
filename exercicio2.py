def somar_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total

# Testes:
print(somar_lista([]))                                      # lista vazia
print(somar_lista([1, 2, 3, 4]))                            # lista de números
print(somar_lista([1, 2, 3, 4, 50, 60, 750, 545312]))       # lista de muitos números

# Saída:
# 0
# 10
# 546182
 