'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Produto: ')).strip().capitalize()
    preço = float(input('Preço: R$ '))
    cont += 1 
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço   
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
         break
print(f'{'FIM DO PROGRAMA':-^40}')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1.000.00 reias')
print(f'O produto mai barato foi {barato} que custa R$ {menor:.2f}')
