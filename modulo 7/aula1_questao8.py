def calcula_digitos_verificadores(cpf):
    # Remove pontos e hífen do CPF
    cpf_numeros = [int(char) for char in cpf if char.isdigit()]
    
    # Calcula primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += cpf_numeros[i] * (10 - i)
    resto = soma % 11
    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto
    
    # Inclui primeiro dígito verificador no cálculo do segundo dígito
    cpf_numeros.append(primeiro_digito)
    
    # Calcula segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += cpf_numeros[i] * (11 - i)
    resto = soma % 11
    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto
    
    return primeiro_digito, segundo_digito

def valida_cpf(cpf):
    # Remove pontos e hífen
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    # Calcula os dígitos verificadores
    primeiro_digito, segundo_digito = calcula_digitos_verificadores(cpf)
    
    # Verifica se os dígitos calculados são iguais aos fornecidos pelo usuário
    if int(cpf[-2]) == primeiro_digito and int(cpf[-1]) == segundo_digito:
        return "Válido"
    else:
        return "Inválido"

# Exemplos de uso
exemplos = [
    "545.315.761-52",
    "545.315.761-12",
    "473.063.662-70",
    "473.063.662-98",
    "775.682.566-77",
    "775.682.566-13"
]

for cpf in exemplos:
    resultado = valida_cpf(cpf)
    print(f"CPF {cpf}: {resultado}")
