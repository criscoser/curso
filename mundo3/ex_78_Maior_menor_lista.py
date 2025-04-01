''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
num = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
       int(input('Digite um numero: ')), int(input('Digite um numero: ')),
       int(input('Digite um numero: ')))
print(f'Voce digitou os valores {num}') #mostra os valores digitados
print(f'O maior valor é {max(num)}, nas posições: ', end='') #mostra o maior valor digitadoa
for i, v in enumerate(num): #percorre a lista para encontrar a posiçao do maior valor
    if v == max(num):
        print(f'{i}... ', end= '')    #mostar as posições do maior valor    
print() #print vazio para quebrar linha
print(f'O menor valor é {min(num)}, nas posiçoes: ', end='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i}...', end='')
print() #print vazio para quebrar linha
