
def list_numbers(number):
    acc = ''
    for n in range(0, int(number)):
        acc += number + ' '
    
    return acc

while True:
    n1 = input('Digite o Numero: ')

    result = list_numbers(n1)

    print('LIST = {}'.format(result))
