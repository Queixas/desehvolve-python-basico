# Todos os números pares entre 20 e 50
numeros_pares = [num for num in range(20, 51, 2)]

# Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
quadrados = [x ** 2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

# Todos os números entre 1 e 100 que sejam divisíveis por 7
divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]

# Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento
paridade = ['par' if num % 2 == 0 else 'ímpar' for num in range(0, 30, 3)]

# Imprimindo os resultados
print("Todos os números pares entre 20 e 50:", numeros_pares)
print("Os quadrados de todos os valores de [1,2,3,4,5,6,7,8,9]:", quadrados)
print("Todos os números entre 1 e 100 que são divisíveis por 7:", divisiveis_por_7)
print("Para todos os valores em range(0,30,3), 'par' ou 'ímpar':", paridade)
