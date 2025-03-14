#Escreva um programa que 
#pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite Km percorridos '))
dias = int(input('Digite por qunato dias '))
valor = dias * 60 + km * 0.15
print(f'o valor é de R$ {valor:.2f} reias')
