"""
Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:
"""


print('=*=' * 15)
print('ANALISADOR DE TRIÂNGULOS')
print('=*=' * 15)
r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmmento '))
r3 = float(input('Terceiro segmento '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar trinângulos!')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos não podem formar triângulo')
