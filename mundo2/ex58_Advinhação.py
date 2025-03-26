"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
computador = randint(0, 10)
print('Adivinhe o numero que pensei de 0 a 10')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais')
        else:
            print('Menos')
print(f'Acertou com {palpites} tentativas!!!')
