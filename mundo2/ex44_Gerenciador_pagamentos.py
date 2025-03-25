"""
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros
"""
preco =  float(input('Digite o valor'))
print(''' FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
op =  int(input('Qual a opção: '))
if  op == 1 :
    total = preco - (preco * 10 / 100)
elif op == 2 :
    total = preco - (preco * 5 / 100)
elif op == 3 :
    total = preco
    parc = total / 2 
    print(f'Sua compra será parcelada em 2X de {parc:.2f}')
elif op == 4 :
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas pracelas ? '))
    parcela = total / totparc 
    print(f'Sua compra será parcelada em {totparc}X de {parcela:.2f},com juros')
print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f}')

