#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome

nome = input('Nome completo ').strip()
print(f'Seu nome em Maiúsculo é {nome.upper()}')
print(f'Seu nome em Minúsculo é {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(' ')} letras')#primeira op~çao

"""
apaga o o print "primeira opção" e usa esse!!!

separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')  #segunda opção

"""