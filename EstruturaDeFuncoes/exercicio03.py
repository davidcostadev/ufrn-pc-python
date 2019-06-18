
def sum(a, b, c):
    return a + b + c

while True:
    n1 = int(input('Primeiro: '))
    n2 = int(input('Segundo: '))
    n3 = int(input('Terceiro: '))

    result = sum(n1, n2, n3)

    print('SOMA = {}'.format(result))
