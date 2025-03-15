"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

"""
print('=*=' * 15)
print('ANALISADOR DE TRIÂNGULOS')
print('=*=' * 15)
r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmmento '))
r3 = float(input('Terceiro segmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('OS segmentos acima PODEM formar trinângulos!')
else:
    print('Os segmentos acima NÃO podem formar triângulos!')
