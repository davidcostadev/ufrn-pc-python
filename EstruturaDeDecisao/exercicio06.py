# https://wiki.python.org.br/EstruturaDeDecisao 
# 06

n1 = float(input('Por favor digite o primeiro número: '))
n2 = float(input('Por favor digite o segundo número: '))
n3 = float(input('Por favor digite o terceiro número: '))


if n1 > n2 and n1 > n3:
    print('O primeiro numero é o maior')
elif n2 > n1 and n2 > n3:
    print('O segundo numero é o maior')
elif n3 > n1 and n3 > n1:
    print('O terceiro numero é o maior')