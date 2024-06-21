import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    frase_embaralhada = []
    
    for palavra in palavras:
        if len(palavra) > 2:  # Embaralhar apenas se a palavra tiver mais de duas letras
            inicio = palavra[0]
            fim = palavra[-1]
            meio = list(palavra[1:-1])  # Lista das letras do meio da palavra
            random.shuffle(meio)  # Embaralhar as letras do meio
            palavra_embaralhada = inicio + ''.join(meio) + fim
        else:
            palavra_embaralhada = palavra  # Se tiver duas ou menos letras, não embaralha
        
        frase_embaralhada.append(palavra_embaralhada)
    
    return ' '.join(frase_embaralhada)

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
