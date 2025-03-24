"""
Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""
from datetime import date
atual = date.today().year
ano = int(input('Ano nascimento: '))
idade = atual - ano
print(f'quem nasceu em {ano} tem {idade} anos em {atual}')
if idade == 18:
    print('deve se alistar IMEDIATAMENTE !')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos, para seu alistamento!')
    ana = atual + saldo
    print(f'seu alistamento será em {ana}')    
elif idade > 18:
    saldo = idade - 18
    print(f'Você ja deveria ter se alistado há {saldo} anos ')
    ana =  atual - saldo
    print(f'seu alistamenteo foi em {ana}')
