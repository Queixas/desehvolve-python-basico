import os

# Solicitar uma frase ao usuário
frase = input("Digite uma frase: ")

# Caminho onde o arquivo será salvo
diretorio_atual = os.getcwd()
caminho_arquivo = os.path.join(diretorio_atual, "frase.txt")

# Abrir o arquivo para escrita
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write(frase)

# Imprimir o caminho completo do arquivo salvo
print(f"Frase salva em {caminho_arquivo}")
