def enesima(num):
    lista = list()
    while num not in lista:
        for n in range(1,num+1):
            lista.append(n)
            x = str(lista).strip('[]').replace(',','')
            print(x)
n = int(input('numero: '))
enesima(n)







        