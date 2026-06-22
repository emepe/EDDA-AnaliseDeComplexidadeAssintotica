def verificar_primeiro(lista):
    if len(lista) == 0:
        return None
    return lista[0]

# Testes:
print(verificar_primeiro([]))                 # lista vazia
print(verificar_primeiro([1, 2, 3, 4]))       # lista de números
print(verificar_primeiro(["a", "b", "c"]))    # lista de strings

# Saída:
# None
# 10
# a