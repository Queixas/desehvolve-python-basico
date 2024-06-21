alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

# Utilizando compreensão de listas para filtrar os alunos aprovados
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

print(aprovados)
