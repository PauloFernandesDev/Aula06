vetorlogin = [""]*5
vetorsenha = [""]*5

for x in range(len(vetorlogin) and len(vetorsenha)):
    vetorlogin[x] = input(f"Digite o login do {x + 1 }° Usuario: ")
    vetorsenha[x] = int(input(f"Digite a senha do {x + 1 }° Usuario: "))

for i in range (len(vetorlogin) and len(vetorsenha)):
    print(f"{i}° Usuario:\nLogin: {vetorlogin[i]}\nSenha: {vetorsenha[i]}\nPosição no Array: {x} \n")