"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida

A fórmula é IMC = peso / (altura x altura). 
"""

peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}, \nvocê esta em ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f}, \nvocê esta em PESO IDEAL!')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f}, \nvocê esta em SOBREPESO!')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f}, \nvocê esta em OBESIDADE!')
elif imc >= 40:
    print(f'Seu IMC é {imc:.1f}, \nvocê esta em OBESIDADE MORBIDA!')

