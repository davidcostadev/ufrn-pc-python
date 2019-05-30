# https://wiki.python.org.br/EstruturaDeDecisao 
# 12

salario = float(input('Qual é o seu salario (Ex: 567.23): '))

if salario > 1500:
    percentual = 5
elif salario > 700:
    percentual = 10
elif salario > 280:
    percentual = 15
else:
    percentual = 20
    
novo_salario = (salario * (percentual+100)) / 100

print('salario antes: {}'.format(salario))
print('percentual aplicado: {}'.format(percentual))
print('valor do aumento: {}'.format(novo_salario - salario))
print('novo salario: {}'.format(novo_salario))

