'''Crie um programa que vai ler vários números e colocar em uma lista.depois disso, mostre:
A) Quantos números foram digitados. 
B) A lista de valores, ordenada de forma decrescente. 
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True: 
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break
print('=' * 30)
print(f'Você digitou {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('o 5 esta presente ')
else:
    print('o 5 não esta presente')
