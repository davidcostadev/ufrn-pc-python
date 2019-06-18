
def check(number):
    if number > 0:
        return 'P'
    else:
        return 'N'

while True:
    n1 = int(input('Digite o Numero: '))

    result = check(n1)

    print('RESULT = {}'.format(result))
