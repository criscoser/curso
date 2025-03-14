# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite seu salário R$ '))
n = s + (s * 15 / 100)
print(f'Novo salário é R$ {n:.3f} reais')
