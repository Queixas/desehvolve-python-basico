def substituir_vogais_por_asterisco(frase):
    vogais = "aeiouAEIOU"
    frase_modificada = ""
    
    for char in frase:
        if char in vogais:
            frase_modificada += "*"
        else:
            frase_modificada += char
    
    return frase_modificada

def main():
    # Solicita uma frase ao usuário
    frase = input("Digite uma frase: ")
    
    # Substitui as vogais por "*"
    frase_modificada = substituir_vogais_por_asterisco(frase)
    
    # Imprime a frase modificada
    print(f"Frase modificada: {frase_modificada}")

if __name__ == "__main__":
    main()
