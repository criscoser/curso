'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

n = list()
impar = list()
par = list()
while True:
    n.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar '))
    if resp in 'Nn':
        break
for i, v in enumerate(n):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Você digitou {n}')
print(f'pares {par}')
print(f'Impares {impar}')
