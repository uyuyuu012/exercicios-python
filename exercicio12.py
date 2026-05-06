menornota = 999999
maiornota = 0
somanotas = 0
qtdnota = 0

while True:
    nota = float(input("Digite sua nota: "))

    if nota == -1:
        break

    qtdnota += 1
    somanotas += nota

    if nota < menornota:
        menornota = nota

    if nota > maiornota:
        maiornota = nota

if qtdnota > 0:
    print("A maior nota foi:", maiornota)
    print("A menor nota foi:", menornota)
    print("A soma das notas foi:", somanotas)
    print("A média das notas é:", somanotas / qtdnota)
else:
    print("Nenhuma nota foi digitada.")