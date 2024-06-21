import csv

# Dados dos livros (título, autor, ano de publicação, número de páginas)
livros = [
    ("Dom Quixote", "Miguel de Cervantes", 1605, 863),
    ("Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417),
    ("A Revolução dos Bichos", "George Orwell", 1945, 144),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96),
    ("1984", "George Orwell", 1949, 336),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223),
    ("O Hobbit", "J.R.R. Tolkien", 1937, 310),
    ("A Menina que Roubava Livros", "Markus Zusak", 2005, 480),
    ("Crime e Castigo", "Fiódor Dostoiévski", 1866, 551),
    ("A Sombra do Vento", "Carlos Ruiz Zafón", 2001, 390)
]

# Nome do arquivo CSV
nome_arquivo = 'meus_livros.csv'

# Abre o arquivo CSV para escrita
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escreve o cabeçalho
    escritor_csv.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    # Escreve os dados dos livros
    for livro in livros:
        escritor_csv.writerow(livro)

print(f'Arquivo "{nome_arquivo}" criado com sucesso!')
