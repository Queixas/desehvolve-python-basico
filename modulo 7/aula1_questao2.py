def main():
    # Solicita o primeiro nome e o sobrenome do usuário
    primeiro_nome = input("Digite seu primeiro nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    
    # Concatena as strings
    nome_completo = primeiro_nome + " " + sobrenome
    
    # Exibe a mensagem de boas-vindas
    print("Bem-vinda,", nome_completo + "!")
    
if __name__ == "__main__":
    main()
