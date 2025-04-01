'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('arroz', 'feijao', 'garrafa', 'vinho', 'pao')
for v in palavras:
    print(f'\nNa palavra {v.upper()} temos ', end='......')
    for letra in v:
        if  letra.lower() in 'aeiou':
            print(letra.upper(), end='-')
