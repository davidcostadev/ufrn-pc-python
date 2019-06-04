number = int(input('Informe o número: '))

is_primo = True

for i in range(2, number - 1):
    r = number % i
    print('{} - {} - {}'.format(number, r, i))
    if r == 0 and (i != 1 or i != number):
        is_primo = False

if is_primo:
    print('É um número primo')
else: 
    print('O {} não é um numero primo'.format(number))