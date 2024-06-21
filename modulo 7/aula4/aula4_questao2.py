import os
import string

# Caminho onde o arquivo foi salvo
diretorio_atual = os.getcwd()
caminho_arquivo_frase = os.path.join(diretorio_atual, "frase.txt")
caminho_arquivo_palavras = os.path.join(diretorio_atual, "palavras.txt")

# Verifica se o arquivo existe
if os.path.exists(caminho_arquivo_frase):
    # Abrir o arquivo de frase para leitura
    with open(caminho_arquivo_frase, 'r') as arquivo_frase:
        # Ler o conteúdo do arquivo
        conteudo = arquivo_frase.read()

    # Remover espaços em branco e caracteres não alfabéticos
    palavras = []
    for palavra in conteudo.split():
        palavra_limpa = ''.join(filter(lambda x: x.isalpha(), palavra))
        if palavra_limpa:
            palavras.append(palavra_limpa.lower())  # Converte para minúsculas
    
    # Escrever as palavras no arquivo palavras.txt
    with open(caminho_arquivo_palavras, 'w') as arquivo_palavras:
        for palavra in palavras:
            arquivo_palavras.write(palavra + '\n')

    # Imprimir o conteúdo do arquivo palavras.txt
    with open(caminho_arquivo_palavras, 'r') as arquivo_palavras:
        conteudo_palavras = arquivo_palavras.read()
    
    print(conteudo_palavras)
else:
    print(f"O arquivo {caminho_arquivo_frase} não foi encontrado.")
