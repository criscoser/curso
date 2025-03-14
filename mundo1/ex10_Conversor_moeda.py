#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

brl = float(input('Digite o valor R$: '))
dol = brl / 5.74
print(f'Com R$ {brl} reais, você compra $ {dol:.2f} dolares')
