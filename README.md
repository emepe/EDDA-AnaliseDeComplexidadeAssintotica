# Exercício – Análise de Complexidade Assintótica (Big O)

- **Disciplina:** Estruturas de Dados e Análise de Algoritmos
- **Aula:** 03 – Notação Assintótica
- **Professor:** Alexandre de Oliveira
- **Aluno:** Maria Paula P. Sousa - 12315841

***
## Exercício 1
```python
 def verificar_primeiro(lista):
    if len(lista) == 0:
        return None
    return lista[0]
```
**Análise:**
- Complexidade: $O(1)$
- Justificativa:  A função executa sempre a mesma quantidade de operações, independente do tamanho da lista. Ela apenas verifica se a lista está vazia e, em seguida, acessa diretamente o primeiro elemento, sem percorrer todos os itens. Por isso, o tempo de execução não cresce com $n$, caracterizando uma complexidade de tempo constante.

***
## Exercício 2
```python
def somar_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total
```
**Análise:**
- Complexidade: $O(n)$
- Justificativa: A função percorre toda a lista uma vez utilizando um laço ``for``, somando cada elemento ao total. Dessa forma, o número de operações cresce proporcionalmente ao tamanho da lista $n$. Não há loops aninhados nem chamadas recursivas adicionais, portanto a complexidade de tempo é linear, $O(n)$.

***
## Exercício 3
```python
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
```
**Análise:**
- Complexidade: $O(log n)$
- Justificativa: A busca binária não percorre a lista inteira; em cada iteração do laço ``while`` ela calcula o índice do meio e descarta metade dos elementos restantes. Isso faz com que o número de comparações cresça de forma proporcional ao logaritmo do tamanho da lista, e não linearmente. Por isso, a complexidade de tempo no pior caso é $O(log n)$.

***
## Exercício 4
```python
def pares_com_soma(lista, alvo):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                print(lista[i], lista[j])
```
**Análise:**
- Complexidade: $O(n²)$
- Justificativa: A função utiliza dois laços ``for`` aninhados que percorrem a lista, gerando todas as combinações de pares de elementos. Para cada posição ``i``, o laço interno testa várias posições ``j``, de modo que o número de comparações cresce proporcionalmente a $n²$. Por isso, a complexidade de tempo no pior caso é quadrática, $O(n²)$.

***
## Exercício 5
```python
def imprimir_pares_e_soma(lista):
    # Bloco 1: imprime cada elemento
    for i in range(len(lista)):
        print(lista[i])

    # Bloco 2: imprime todos os pares
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i], lista[j])
```
**Análise:**
- Complexidade: $O(n^2)$
- Justificativa: A função é composta por dois blocos. O primeiro percorre a lista uma vez, tendo complexidade $O(n)$. O segundo possui dois laços ``for`` aninhados que geram todos os pares de elementos, resultando em $O(n^2)$ operações. Como $O(n^2)$ domina $O(n)$, a complexidade de tempo no pior caso é quadrática, $O(n^2)$.

***
## Exercício 6
```python
def potencias_de_dois(n):
    i = 1
    while i < n:
        print(i)
        i *= 2
```
**Análise:**
- Complexidade: $O(log n)$
- Justificativa: A função não percorre todos os valores até $n$; em vez disso, a variável ``i`` é multiplicada por 2 a cada iteração do laço ``while``. Isso faz com que o número de repetição do laço cresça proporcionalmente ao logaritmo de $n$, pois basta dobrar ``i`` algumas vezes até que ele alcance ou ultrapasse $n$. Assim, a complexidade de tempo no pior caso é $O(log n)$.


***
## Exercício 7
```python
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
```
**Análise:**
- Complexidade: $O(2^n)$
- Justificativa: A implementação recursiva do Fibonacci faz duas chamadas recursivas para quase todos os valores de ``n (f(n - 1)$`` e ``f(n - 2))``, gerando uma árvore de chamadas que cresce exponencialmente. Muitos subproblemas são recalculados diversas vezes, o que faz o número total de chamadas quase dobrar a cada incremento de $n$. Por isso, a complexidade de tempo no pior caso é exponencial, $O(2^n)$.

***
## Exercício 8
```python
def ordenacao_bolha(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
```
**Análise:**
- Complexidade: $O(n^2)$
- Justificativa: O algoritmo de ordenação bolha utiliza dois laços ``for`` aninhados. O laço externo percorre a lista ``n`` vezes e, para cada iteração, o laço interno percorre quase todos os elementos restantes, realizando comparações e possíveis trocas entre pares adjacentes. O número total de operações cresce proporcionalmente a $n^2$, caracterizando uma complexidade de tempo quadrática, $O(n^2)$.

***
## Exercício 9
```python
def produto_de_matrizes(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
```
**Análise:**
- Complexidade: $O(n^3)$ 
- Justificativa: A função utiliza três laços ``for`` aninhados, cada um percorrendo ``n`` posições da matriz. Para cada par de índices ``(i, j)``, o laço interno em ``k`` realiza ``n`` multiplicações e somas para calcular o elemento ``C[i][j]``. Como o número total de operações é proporcional ``a n × n × n``, a complexidade de tempo no pior caso é cúbica, $O(n³)$.

***
## Exercício 10
```python
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
```
**Análise:**
- Complexidade: $O(n log n)$
- Justificativa: O merge sort divide recursivamente a lista ao meio até obter sublistas de tamanho 1, o que gera aproximadamente $log n$ níveis de recursão. Em cada nível, o passo de mesclagem percorre todos os elementos das sublistas para intercalar os valores em ordem, realizando trabalho proporcional a $n$. Com isso, o custo total é $n$ em cada nível vezes $log n$ níveis, resultando em uma complexidade de tempo $O(n log n)$.
