def main():
    frase = input("Digite uma frase: ")
    
    # Obtendo todas as letras da frase (considerando maiúsculas e minúsculas)
    letras = [letra for letra in frase if letra.isalpha()]
    
    # Separando vogais e consoantes
    vogais = [letra.lower() for letra in letras if letra.lower() in 'aeiou']
    consoantes = [letra for letra in letras if letra.lower() not in 'aeiou']
    
    # Ordenando vogais alfabeticamente
    vogais_ordenadas = sorted(vogais)
    
    # Imprimindo resultados
    print("Vogais:", vogais_ordenadas)
    print("Consoantes:", consoantes)

if __name__ == "__main__":
    main()
