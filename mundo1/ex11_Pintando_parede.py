#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

alt = float(input('Altura: '))
larg = float(input('Largura: '))
are = alt * larg
tinta =  are / 2 
print(f'área é de {are} metros², e você precisa de {tinta} litros  para pintar')
