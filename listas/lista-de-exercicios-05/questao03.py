def valor_compras(carne,arroz,feijao):
 soma_precos = carne + arroz + feijao
 return soma_precos
 
 
compra1 = float(input('valor da carne : '))
compra2 = float(input('valor do arroz : '))
compra3 = float(input('valor do feijão : '))
resultado = valor_compras(compra1,compra2,compra3)
print(resultado)
