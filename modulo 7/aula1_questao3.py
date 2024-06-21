def contar_espacos(frase):
    # Inicializa o contador de espaços em branco
    contador = 0
    
    # Itera através de cada caractere na frase
    for caractere in frase:
        if caractere == ' ':
            contador += 1
    
    return contador

def main():
    # Solicita ao usuário que digite a frase
    frase = input("Digite a frase: ")
    
    # Chama a função para contar os espaços em branco
    espacos_em_branco = contar_espacos(frase)
    
    # Exibe o resultado
    print("Espaços em branco:", espacos_em_branco)

if __name__ == "__main__":
    main()
