sum = 0

for i in range(1, 6):
    number = float(input('Informe o Nº({}): '.format(i)))
    sum += number

print('\nCalculando...\n')

print('SOMA={}'.format(sum))
print('MEDIA={}'.format(sum / 5))