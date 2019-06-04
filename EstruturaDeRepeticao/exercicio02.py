
is_valid = False

while is_valid == False:
    username = input('Informe seu Username: ')
    password = input('Digite sua senha: ')

    if username == 'davidcosta' and password == 'asdf':
        is_valid = True
    else:
        print('Você digitou um username ou uma Senha inválida.\n')
        
print('\nBem vindo')