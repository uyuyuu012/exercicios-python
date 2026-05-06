vendedor = int(input("Digite o seu código: "))
peca=int(input("Digite o código da peça: "))
preco = float(input("Digite o valor unitário da peça: "))
qtd_vendida = int(input("Digite a quantidade de peças que foram venidadas: "))

venda_total = preco * qtd_vendida

print ("O código do vendedor é: ",vendedor,"O código da peça vendida é: ",peca,"O preço de um é: R$",preco)

print ("O total da comissão é: R$",venda_total*0.05)