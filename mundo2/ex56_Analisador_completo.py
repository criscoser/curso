"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f' ---- {c}° PESSOA ---- ')
    nome = str(input('Nome: ')).strip() 
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:  ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm' :
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome 
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
 
mediaidade = somaidade / 4
print(f'O nome do mais velho tem {maioridadehomem} e se chama {nomevelho}')
print(f'A média de idade é {mediaidade}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos ')

    
    
    

