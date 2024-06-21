def nome_mes(mes):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    return meses[mes - 1]

def main():
    # Solicita a data de nascimento ao usuário
    data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
    
    # Separa dia, mês e ano
    dia, mes, ano = data_nascimento.split('/')
    
    # Converte para inteiros
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    
    # Obtém o nome do mês por extenso
    nome_do_mes = nome_mes(mes)
    
    # Imprime a data formatada
    print(f"Você nasceu em {dia} de {nome_do_mes} de {ano}.")

if __name__ == "__main__":
    main()
