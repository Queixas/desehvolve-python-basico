def formatar_numero(numero):
    # Converte o número para string para facilitar a manipulação
    numero_str = str(numero)
    
    # Verifica o comprimento do número
    if len(numero_str) == 8:
        numero_completo = "9" + numero_str  # Adiciona o 9 na frente
    elif len(numero_str) == 9:
        if numero_str[0] == '9':
            numero_completo = numero_str[:5] + "-" + numero_str[5:]  # Insere o separador "-"
        else:
            numero_completo = numero_str  # Não faz alteração se não começa com 9
    else:
        numero_completo = numero_str  # Mantém o número original se for de outro formato
    
    return numero_completo

def main():
    # Solicita ao usuário que digite o número de celular
    numero = input("Digite o número: ")
    
    # Chama a função para formatar o número
    numero_formatado = formatar_numero(numero)
    
    # Exibe o número formatado
    print("Número completo:", numero_formatado)

if __name__ == "__main__":
    main()
