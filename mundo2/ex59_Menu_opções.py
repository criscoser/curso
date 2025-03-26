"""Crie um programa que leia dois valores e mostre um menu na 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

n1 = int(input('Digite um número: '))
n2 = int(input('digite mais um números: '))
op = 0
while op != 5:
    print('''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] Sair
''')
    op = int(input('Qual sua opção: '))
    if op == 1:
        soma = n1 + n2
        print(f'A soma é {soma}')
    elif op == 2:
        multi = n1 * n2
        print(f'A multiplicação é {multi}')
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f' O maior é {maior}')
    elif op  == 4:
        print('Informe os numeros novamnete ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando')
    else:
        print('Opção inválida!')
print('FIM!!!!')
