'''Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

while True:
    n = int(input('Digite um número para ver sua tabuada [-1 PARAR]: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:2} = {n*c:2}')
print('Acabou')
