import random

def gerar_lista_aleatoria(tamanho):
    lista = [random.randint(-10, 10) for _ in range(tamanho)]
    return lista

def encontrar_maior_intervalo_negativo(lista):
    maior_inicio = 0
    maior_fim = 0
    maior_contagem = 0
    
    inicio = 0
    while inicio < len(lista):
        if lista[inicio] < 0:
            fim = inicio
            while fim < len(lista) and lista[fim] < 0:
                fim += 1
            contagem = fim - inicio
            if contagem > maior_contagem:
                maior_contagem = contagem
                maior_inicio = inicio
                maior_fim = fim
            inicio = fim
        else:
            inicio += 1
    
    return maior_inicio, maior_fim

def main():
    lista = gerar_lista_aleatoria(20)
    print("Original:", lista)
    
    inicio, fim = encontrar_maior_intervalo_negativo(lista)
    del lista[inicio:fim]
    
    print("Editada:", lista)

if __name__ == "__main__":
    main()
