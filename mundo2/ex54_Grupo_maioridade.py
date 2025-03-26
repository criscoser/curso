"""
 Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. 
"""


from datetime import date
atual = date.today().year
contmai = 0
contmen = 0 
for c in range(1, 7):    
    data = int(input(f'Em que ano a {c}° nasceu? '))
    idade = atual - data
    print(idade)
    if idade < 18 :
        contmen += 1 
    else:
        contmai += 1
print(f'{contmen} pessoas Menores de idade')
print(f'{contmai} pessoas Maiores de idade')
