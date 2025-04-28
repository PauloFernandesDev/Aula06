notas = [""]*5
media = 0
cont = 0
for x in range(len(notas)):
    notas[x] = float(input(f"Digite a nota do {x+1}° aluno:"))

for z in notas:
    media += z

media = media / len(notas)

for y in notas:
    if y > media :
        cont += 1

print(f"Media da turma: {media}, Quantidade de alunos acima da media: {cont}")