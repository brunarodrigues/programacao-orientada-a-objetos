def reverso(num):
    reverte = num[::-1]
    return reverte

numero = input('numero: ')
f = reverso(numero)
print('reverso: {}'.format(f))
