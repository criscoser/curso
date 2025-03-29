'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

times = ('Atlético', 'Mineiro', 'Bahia', 'Botafogo', 'Ceará', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude',
         'Mirassol', 'Palmeiras', 'Red Bull Bragantino', 'Santos', 'São Paulo', 'Sport', 'Vasco da Gama', 'Vitória')
print(f'Os 5 prmeiros são  {times[0:5]}')
print(f'Os 4 últimos colocados são {times[17:]}')
print('EM ORDEM ALFABETICA É:')
print("\n".join(sorted(times)))

