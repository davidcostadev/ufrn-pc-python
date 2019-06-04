while True:
    number = float(input('Digite uma nota: '))

    if number >= 0 and number <= 10:
        print('Válido.')
        break
    else:
        print('Inválido.')