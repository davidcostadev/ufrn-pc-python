n_esimo = int(input('Informe o n-esimo: '))

result = 1
last = 0
serie =[]

for i in range(0, n_esimo):
    temp = result
    result = result + last
    last = temp

    serie.append(result)

print(serie)
