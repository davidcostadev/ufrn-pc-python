# https://wiki.python.org.br/EstruturaDeDecisao 
# 1

first = float(input('Enter the first number: '))
second = float(input('Enter the second number: '))

if first > second:
    print('The number first number({}) greater than second number({}).'.format(first, second))
elif second > first:
    print('The number second number({}) greater than first number({}).'.format(second, first))
else:
    print('They are the same.')
