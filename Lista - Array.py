"""
Percorrer a lista
    1° forma(todas as linguagens):
                for x in range(len(compras)):
                    print(compras[x])
    2° forma(python):
                for y in frutas:
                    print(y)

            obs:percorre pelo conteudo!

Adicionar um item no final da lista:
    compras.append(["limão, "mamao"])
    compras.append(

Inserir um item na posição especifica da lista:
    compras.insert(_index: 1,_object: "Tomate")

"""

alunos  = [""]*5

for x in range(0,len(alunos)):
    alunos[x] = input(f"Digite o nome do {x +1}° Aluno: ")

print(f"Alunos : {alunos}", end=" ")
