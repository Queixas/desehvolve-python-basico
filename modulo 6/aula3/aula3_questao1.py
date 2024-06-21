#1) Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
#A lista original
#Os 3 primeiros elementos
#Os 2 últimos elementos
#A lista invertida (do fim para o começo)
#Os elementos de índice par (0, 2, 4 … )
#Os elementos de índice ímpar (1, 3, 5, … )
def solicitar_numeros():
    numeros = []
    
    while len(numeros) < 4:
        try:
            numero = int(input("Digite um número inteiro (mínimo de 4 valores): "))
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um valor inteiro válido.")
    
    while True:
        try:
            numero = int(input("Digite mais um número inteiro ou 'q' para parar: "))
            numeros.append(numero)
        except ValueError:
            print("Finalizando a entrada de números.")
            break
    
    return numeros

def main():
    numeros = solicitar_numeros()
    
    print("Lista original:", numeros)
    print("Os 3 primeiros elementos:", numeros[:3])
    print("Os 2 últimos elementos:", numeros[-2:])
    print("A lista invertida:", numeros[::-1])
    print("Elementos de índice par:", numeros[::2])
    print("Elementos de índice ímpar:", numeros[1::2])

if __name__ == "__main__":
    main()
