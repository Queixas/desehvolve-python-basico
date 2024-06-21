def sao_anagramas(palavra1, palavra2):
    # Remove espaços em branco e converte para letras minúsculas
    palavra1 = palavra1.lower().replace(" ", "")
    palavra2 = palavra2.lower().replace(" ", "")
    
    # Verifica se as palavras têm o mesmo comprimento
    if len(palavra1) != len(palavra2):
        return False
    
    # Ordena as letras das palavras e verifica se são iguais
    return sorted(palavra1) == sorted(palavra2)

def encontrar_anagramas(frase, objetivo):
    # Dividir a frase em palavras
    palavras = frase.split()
    
    # Lista para armazenar os anagramas encontrados
    anagramas = []
    
    # Itera sobre cada palavra na lista de palavras
    for palavra in palavras:
        if sao_anagramas(palavra, objetivo):
            anagramas.append(palavra)
    
    return anagramas

def main():
    # Solicita ao usuário que digite a frase e a palavra objetivo
    frase = input("Digite uma frase: ")
    objetivo = input("Digite a palavra objetivo: ")
    
    # Encontra os anagramas da palavra objetivo na frase
    anagramas = encontrar_anagramas(frase, objetivo)
    
    # Exibe os anagramas encontrados
    print(f"Anagramas: {anagramas}")

if __name__ == "__main__":
    main()
