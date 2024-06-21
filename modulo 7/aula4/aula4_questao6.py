import csv
import os

# Caminho do arquivo
nome_arquivo = 'modulo 7\\aula4\\spotify-2023.csv'

# Verifica se o arquivo existe antes de tentar abri-lo
if os.path.exists(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', encoding='latin-1') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            
            # Lista para armazenar as músicas mais tocadas por ano
            musicas_mais_tocadas = []

            # Ignorar o cabeçalho
            next(leitor_csv)

            # Dicionário para armazenar a música mais tocada de cada ano
            musicas_por_ano = {}

            # Percorre as linhas do arquivo CSV
            for linha in leitor_csv:
                try:
                    # Captura os dados relevantes da linha
                    track_name = linha[0]
                    artist_name = linha[1]
                    artist_count = int(linha[2])
                    released_year = int(linha[3])
                    streams = int(linha[8])

                    # Verifica se o ano está no intervalo desejado (2012-2022)
                    if 2012 <= released_year <= 2022:
                        # Se não houver música registrada para o ano ou se esta música tem mais streams, atualiza
                        if released_year not in musicas_por_ano or streams > musicas_por_ano[released_year][3]:
                            musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]
                except ValueError:
                    continue

            # Monta a lista com as músicas mais tocadas por ano
            for ano in range(2012, 2023):
                if ano in musicas_por_ano:
                    musicas_mais_tocadas.append(musicas_por_ano[ano])

            # Imprime a lista de músicas mais tocadas por ano
            print(musicas_mais_tocadas)

    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Verifique o caminho do arquivo.")

else:
    print(f"Arquivo '{nome_arquivo}' não encontrado. Verifique o caminho do arquivo.")
