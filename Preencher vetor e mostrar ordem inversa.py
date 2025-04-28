vetor = [""]*5
for x in range (len(vetor)):
    vetor[x] = int(input(f"Digite o {x+1}° valor: "))

for i in range (len(vetor) -1 ,-1,-1):
    print(vetor[i], end=" ")