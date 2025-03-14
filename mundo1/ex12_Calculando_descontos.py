#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
n = float(input('Digite o preço R$ '))
np = n - (n * 5 / 100)
print(f'o valor com 5% de desconto é R$ {np:.2f}')
