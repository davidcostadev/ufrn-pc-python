first = float(input('Digite a primeira nota: '))
second = float(input('Digite a segunda nota: '))
third = float(input('Digite a terceira nota: '))

media = (first + second + third) / 3

if media >= 7:
    print('Aprovado com média maior ou igual a 7.')
elif media >= 5:
    if first >= 3 and second >= 3 and third >= 3:
        print('Aprovado com média maior ou igual a 5.')
    else:
        print('Você foi reprovado, você possui uma nota abaixo de 3.')
else:
    print('Você foi reprovado.')

