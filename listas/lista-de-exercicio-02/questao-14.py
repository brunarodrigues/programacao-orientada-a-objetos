peso = float(input('Digite o peso do peixe:'))
if peso>50:
  excesso = peso-50
  multa = excesso*4
  print('A cada peso do peixe maior que o estabelecido a multa será: {:.2f}'.format(multa))
else:
    excesso = 'zero'
    multa = 'zero'
    print('O peso do peixe não é maior que o estabelecido ou seja a multa será : {}'.format(multa))