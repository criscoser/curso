#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}')
cos = math.cos(math.radians(ang))
print(f'O ângulo de {ang} tem o COSSENO de {cos:.2f}')
tang = math.tan(math.radians(ang))
print(f'O ângulo de {ang} tem a TANGENTE de {tang:.2f}')

