vetorA = [""]*5
vetorM = [""]*5

for i in range (len(vetorA)):
    vetorA[i] = int(input(f"Digite o {i + 1}° valor do vetor A: "))

x = int(input("Digite valor para multiplicar: "))

for y in  range(len(vetorA)):
    vetorM[y] = vetorA[y] * x

print(vetorA)
print(f"x{x}")
print(vetorM)
