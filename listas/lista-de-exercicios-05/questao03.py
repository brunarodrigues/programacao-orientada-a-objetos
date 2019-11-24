def soma(num1,num2,num3):
    soma = (num1 + num2 + num3)
    
    return soma

n1,n2,n3 = input('digite 3 numeros: ').split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
x = soma(n1,n2,n3)
print('a soma entre {}, {}, {} = {}'.format(n1,n2,n3,x))