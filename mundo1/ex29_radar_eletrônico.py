"""
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.

"""
vel = int(input('Digite a velocidade: '))
if vel > 80:
    multa = 7 + vel - 80
    print(f'sua velocidae é de {vel} ')
    print(f' e a multa é de R$ {multa:.2f} reais')
else:
    print('Faça uma ótima viagem!')
