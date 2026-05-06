nome = (input("Digite o seu nome: "))
senha1 = 12345678

senha2 = int(input("Digite a sua senha: "))
i = 1
while i <= 3:
    if senha2 == senha1:
        print("Acesso permitido")
        break
    else:
        if i<3:
            i += 1
            senha2 = int(input("Digite a sua senha novamente: "))
        else:
            print("Acesso negado")
            break