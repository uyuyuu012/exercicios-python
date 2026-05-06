altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura*altura)

print ("O seu IMC é de: ",imc)
if imc < 18.5:
    print("A sua classificação é: abaixo do peso normal")
elif imc >= 18.5 and imc <=24.9:
    print("A sua classificação é: peso normal")
elif imc >= 25 and imc <=29.9:
    print("A sua classificação é: excesso de peso")
elif imc >= 30 and imc <=34.9:
    print("A sua classificação é: obesidade classe I")
elif imc >= 35 and imc <= 39.9:
    print("A sua classificação é: obesidade classe II")
else:
    print("A sua classificação é: obesidade classe III")