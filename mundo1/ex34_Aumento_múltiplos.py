"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

"""
s = float(input('Digite seu Sálario R$ '))
if s > 1.250:
    ns = s + (s * 10 / 100)
if s <= 1.250:
    ns = s + (s * 15 / 100)
print(f'Seu novo salário é R$ {ns:.3f} reais')
