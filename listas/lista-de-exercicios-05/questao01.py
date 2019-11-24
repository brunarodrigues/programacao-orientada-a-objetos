def enesima (num):
    for l in range(1,num+1):
        print('{} {}'.format(l,'')*l)

num = int(input('Numero: '))
x = enesima(num)