'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
a = int(input('Digite o 1° Número '))
b = int(input('Digite o 2° Número '))
c = int(input('Digite o 3° Número '))
#Verificando quem pe MENOR
menor = a
if b < a and b < c:
    menor = c 
if c < a and c < b:
    menor = c
# Verificando quem é o MAIOR
maior = a 
if b > a and b > c:
     maior = b
if c > a and c > b:
    maior = c
print(f'O MAIOR é {maior}')         
print(f'O MENOR é {menor}')
