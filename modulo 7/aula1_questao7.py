import random

def encrypt(nomes):
    # Gerar uma chave de criptografia aleatória entre 1 e 10
    chave_aleatoria = random.randint(1, 10)
    
    # Lista para armazenar os nomes criptografados
    nomes_criptografados = []
    
    # Iterar sobre cada nome na lista de nomes
    for nome in nomes:
        nome_criptografado = ''
        # Criptografar cada caractere no nome
        for char in nome:
            # Verificar se o caractere está no intervalo visível (33 a 126 na tabela Unicode)
            if ord(char) >= 33 and ord(char) <= 126:
                # Criptografar o caractere
                codigo_cripto = ord(char) + chave_aleatoria
                if codigo_cripto > 126:
                    codigo_cripto -= 94  # Voltar ao início do intervalo visível
                nome_criptografado += chr(codigo_cripto)
            else:
                # Manter caracteres fora do intervalo visível sem criptografia
                nome_criptografado += char
        
        # Adicionar nome criptografado à lista
        nomes_criptografados.append(nome_criptografado)
    
    # Retornar nomes criptografados e a chave aleatória
    return nomes_criptografados, chave_aleatoria

# Exemplo de uso
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave_aleatoria = encrypt(nomes)

# Imprimir resultados
print("Nomes Criptografados:", nomes_criptografados)
print("Chave de Criptografia:", chave_aleatoria)
