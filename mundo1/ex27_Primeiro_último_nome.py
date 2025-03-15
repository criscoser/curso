#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite seu nome completo ')).strip().upper()
nome = n.split()
print(f'Prazer em te conhecer {n}')
print(f'seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome) - 1]}')

