#Escreva um programa que solicita o nome do usuário e o imprime em forma de escada,

def main():
    # Solicita o nome do usuário
    nome = input("Digite seu nome: ")
    
    # Loop para construir a escada
    for i in range(1, len(nome) + 1):
        # Imprime a substring do início até o índice i
        print(nome[:i])

if __name__ == "__main__":
    main()
