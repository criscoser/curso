#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n1 = int(input('Informe um número '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print(f'Analisando o numero {n1}')
print(f'Unidade é: {u}')
print(f'Dezena é:  {d}')
print(f'Centena é: {c}')
print(f'Milhar é:  {m}')
