def soma_imposto(taxa,custo):
    c = custo+(taxa/100)*custo
    return c

preco = float(input('porcentagem: '))
custo = float(input('produto: '))
y = soma_imposto(preco,custo)
print('valor: R$ {:.2f}'.format(y))