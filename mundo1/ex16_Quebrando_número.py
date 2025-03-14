
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input('Digite um valor '))
print(f'o valor digitado foi {num} e sua porção inteira é {trunc(num)}')



# SEGUNDA OPÇÃO!!! sem importar a biblioteca
"""
num = float(input('digite um valor '))
print(f'O vamor digitado foi {num} e sua porção inteira é {int(num)}')
"""