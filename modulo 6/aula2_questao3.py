#3) Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50.
# Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas.
# Ao final imprima:
#Ambas as listas
#A lista intersecção ordenada
#A quantidade de vezes que cada elemento aparece em cada lista
#Atenção, a lista de intersecções não pode ter duplicatas. Segue um exemplo da saída esperada.
#lista1 - [10, 10, 28, 10, 29, 20, 30, 10, 29, 11]
#lista2 - [11, 16, 26, 44, 11, 10, 20, 29, 10, 12]
#Interseccao - [10, 11, 20]
#Contagem
#10: (lista1=4, lista2=1)
#11: (lista1=1, lista2=2)
#20: (lista1=1, lista2=1)
import random
lista1,lista2,lista3=[],[],[]
for i in range(1,21):
    a=random.randint(0,50)
    lista1.append(a)
    b=random.randint(0,50)
    lista2.append(b)
    if a in lista2:
        if a not in lista3:
            lista3.append(a)
    if b in lista1:
        if b not in lista3:
            lista3.append(b)
print(f"Lista 1 - {lista1} Lista 2 - {lista2}")
print(f"Interseção - {lista3}")

for i in lista3:
    print(f"Número {i}: Aparece na lista1 {lista1.count(i)} vezes e {lista2.count(i)} vezes na lista2")



