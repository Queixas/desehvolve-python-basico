# Definir o caminho para o arquivo local
caminho_arquivo = 'caminho_para_o_arquivo/estomago.txt'  # Substitua pelo caminho correto no seu sistema

# Abrir o arquivo para leitura
with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    # Ler as primeiras 25 linhas
    print("Texto das primeiras 25 linhas:")
    for i in range(25):
        linha = arquivo.readline().strip()  # Strip remove espaços em branco e quebras de linha extras
        print(linha)
    
    # Voltar ao início do arquivo para contar o número total de linhas
    arquivo.seek(0)
    total_linhas = sum(1 for linha in arquivo)
    print(f"\nNúmero total de linhas do arquivo: {total_linhas}")
    
    # Encontrar a linha com maior número de caracteres
    arquivo.seek(0)
    maior_linha = max((linha.strip() for linha in arquivo), key=len)
    print(f"\nLinha com maior número de caracteres:\n{maior_linha}")
    
    # Contar menções aos nomes "Nonato" e "Íria"
    arquivo.seek(0)
    texto_completo = arquivo.read().lower()  # Convertendo para minúsculas para facilitar a busca
    contagem_nonato = texto_completo.count('nonato')
    contagem_iria = texto_completo.count('íria')
    
    print(f"\nNúmero de menções aos nomes 'Nonato' e 'Íria':")
    print(f"Nonato: {contagem_nonato}")
    print(f"Íria: {contagem_iria}")
