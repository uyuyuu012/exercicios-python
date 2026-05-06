valorI = float(input("Digite o preço de fábrica do carro: "))
lucro = ((valorI/100)*12)
imposto = ((valorI/100)*45)
valorF = valorI + imposto + lucro
print("O valor final é de",valorF,"o imposto foi de",imposto,"e o lucro foi de",lucro)