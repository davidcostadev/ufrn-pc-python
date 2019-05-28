# https://wiki.python.org.br/EstruturaDeDecisao 
# 2

number = float(input('Enter the number: '))

if number > 0:
    print('The number {} is positive'.format(number))
elif number < 0:
    print('The number {} is negative.'.format(number))
else:
    print('The number is zero')
