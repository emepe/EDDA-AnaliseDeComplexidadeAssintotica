def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Testes:
for i in range(6):
    print(i, "->", fibonacci_recursivo(i))

print(fibonacci_recursivo(10))

print(fibonacci_recursivo(20))

# Saídas:

# 0 -> 0
# 1 -> 1
# 2 -> 1
# 3 -> 2
# 4 -> 3
# 5 -> 5
# 55
# 6765