usuarios = 0 
adultos = 0
while usuarios != -1:
    nome = input("Digite o nome do usuário (ou 'encerrar' para sair): ")
    
    if nome == 'encerrar' or nome == 'Encerrar':
        break
    
    idade = int(input("Digita a idade do usuário: "))
    usuarios += 1
    if idade >= 18:
       adultos += 1
        
print("Quantidade de usuários: ", usuarios)
print("Quantidade de adultos: ", adultos)