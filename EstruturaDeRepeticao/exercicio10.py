first = int(input('Informe o primeiro número: '))
second = int(input('Informe o segundo número: '))

if second > first:
    x = first
    y = second + 1  
    step = 1
else:
    x = first
    y = second - 1
    step = -1

for number in range(x, y, step): 
    print(number)