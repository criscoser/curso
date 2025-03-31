'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
import random

numeros = list(range(0,11))
escolha = random.sample(numeros, 5)
print(f' OS numeros são{escolha}')
print(f'Maior valor {max(escolha)}')
print(f'Menor valor {min(escolha)}')
