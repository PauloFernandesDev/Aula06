vetorlogin = ["joao","carlos","mario","maria","josefa"]
vetorsenha = [1234,3432,5432,3333,6666]
validar = False
login = input("Login: ")
senha = int(input("Senha: "))

for x in range (len(vetorlogin)):
    if login == vetorlogin[x] and senha == vetorsenha[x]:
        print(f"Login efetuado com sucesso! \nBem vindo {vetorlogin[x]}!")
        validar = True

if not validar:
    print("Login ou Senha invalida!!!.")