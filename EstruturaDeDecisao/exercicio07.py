# https://wiki.python.org.br/EstruturaDeDecisao 
# 07

n1 = float(input('Por favor digite o primeiro número: '))
n2 = float(input('Por favor digite o segundo número: '))
n3 = float(input('Por favor digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    maior = 'primeiro'
elif n2 > n1 and n2 > n3:
    maior = 'segundo'
elif n3 > n1 and n3 > n1:
    maior = 'terceiro'

if n1 < n2 and n1 < n3:
    menor = 'primeiro'
elif n2 < n1 and n2 < n3:
    menor = 'segundo'
elif n3 < n1 and n3 < n1:
    menor = 'terceiro'

print('O maior é: {} e o menor é: {}'.format(maior, menor))