# https://wiki.python.org.br/EstruturaDeDecisao 
# 05

letra = input('Por favor digite uma letra: ').lower()

vogal = 'a,e,i,o,u'.split(',')
consoante = 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,x,w,z'.split(',')

is_vogal = False
is_consoante = False

for i in vogal:
    if letra == i:
        is_vogal = True
        print('É uma vogal')

if not is_vogal:
    for j in consoante:
        if letra == j:
            is_consoante = True
            print('É uma consoante')

if not is_vogal and not is_consoante:
    print('Não é uma letra')


