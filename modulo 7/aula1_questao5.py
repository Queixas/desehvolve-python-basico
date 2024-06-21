def contar_vogais_e_indices(frase):
    # Lista de vogais
    vogais = "aeiouAEIOU"
    
    # Inicializa o contador de vogais
    contador_vogais = 0
    
    # Lista para armazenar os índices das vogais
    indices_vogais = []
    
    # Itera através de cada caractere na frase
    for indice, caractere in enumerate(frase):
        if caractere in vogais:
            contador_vogais += 1
            indices_vogais.append(indice)
    
    return contador_vogais, indices_vogais

def main():
    # Solicita ao usuário que digite a frase
    frase = input("Digite uma frase: ")
    
    # Chama a função para contar vogais e obter os índices
    num_vogais, indices_vogais = contar_vogais_e_indices(frase)
    
    # Exibe o número de vogais
    print(f"{num_vogais} vogais")
    
    # Exibe os índices das vogais
    print(f"Índices {indices_vogais}")

if __name__ == "__main__":
    main()
