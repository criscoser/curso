"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

casa = float(input("Valor da casa R$: "))
salario = float(input('Salário do comprador R$: '))
anos = int(input('Qauntos anos pra pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Pra pagar a casa de R$ {casa:.2f} em {anos} anos ', end='')
print(f'A prestação será de R$ {prestacao:.2f} reais')
if prestacao <= minimo:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')
