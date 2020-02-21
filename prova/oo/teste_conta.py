def cria_conta(titular,numero,saldo,limite):
    conta = {"titular": titular, "numero": numero,"saldo": saldo, "limite": limite}
    return conta 

def deposita(conta,valor):
    #conta na posiçao saldo é igual conta na posiçao saldo mais valor
    conta['saldo']+= valor

def saca(conta,valor):
    conta['saldo']-= valor

def extrato(conta):
    print(f'conta: {conta['numero']}\nsaldo: {conta['saldo']}')