nomes = ["Joao", "Carlos","Ana", "Maria","Pitomba"]
encontrado = False
nome = input("Digite o nome para encontrar: ")
for x in range(len(nomes)):
    if nomes[x] == nome:
        print(f"Encontrei! posição na lista: {x} ")
        encontrado = True

if not encontrado:
    print("Nome não encontrado!")

