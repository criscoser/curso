'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

lista = ('prod1',10, 'prod2', 2.5, 'prod3', 11.25, 'prod4', 3.75)
print('=' * 40)
print(f'{"lISTA DE COMPRAS":^40}')
print('=' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R$ {lista[pos]:>5.2f}')
