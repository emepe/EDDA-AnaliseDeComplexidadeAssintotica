def potencias_de_dois(n):
    i = 1
    while i < n:
        print(i)
        i *= 2

potencias_de_dois(1)   # Saída: não deve imprimir nada

potencias_de_dois(10)  # Saída: 1, 2, 4, 8

potencias_de_dois(20)  # Saída: 1, 2, 4, 8, 16

potencias_de_dois(100) # Saída: 1, 2, 4, 8, 16, 32, 64