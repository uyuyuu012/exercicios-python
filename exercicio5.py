salarioA = float(input("Digite o seu salário: "))
nome = str(input("Digite o seu nome: "))
if (salarioA < 1000 and salarioA > 0):
    salafrioF = ((salarioA/100)*20)+salarioA
elif(salarioA > 1000.1 and salarioA < 5000):
    salafrioF = ((salarioA/100)*10)+salarioA
else:
    salafrioF = ((salarioA/100)*5)+salarioA
print("O novo salário do jogador",nome,"é:",salafrioF)