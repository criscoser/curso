"""
Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO
"""

nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a segunda nota '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Sua nota é {media:.2f}, REPROVADO!')
elif media > 5.1 and media < 6.9:
    print(f'Sua nota é {media:.2f}, RECUPERAÇÃO!')
elif media > 7.0 and media < 9.0:
    print(f'Sua nota é {media:.2f}, APROVADO')
elif media >= 9.1:
    print(f'Sua nota é {media:.2f}')
    print(f'PARABENS, APROVADO COM LOUVOR, CONTINUE ASSIM!!!')
