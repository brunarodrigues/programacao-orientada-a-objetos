sexo = input('Digite seu sexo:')
alt = float(input('Digite sua altura:'))
def peso_ideal (sexo,altura):
  if (sexo == 'masculino'):
    calculo=(72.7*alt)-58    
    return calculo
  elif(sexo=='feminino'):
    calculo2=(62.1*alt)-44.7
    return calculo2

peso = peso_ideal(sexo,alt)

print('Seu peso ideal é:{:.2f}'.format(peso))