def cria_conta(titular,numero,saldo,limite):
    '''cria uma conta'''

    conta = {"titular": titular, "numero": numero,"saldo": saldo, "limite": limite}
    return conta 

def deposita(conta,valor):
    #conta na posiçao saldo é igual conta na posiçao saldo mais valor
    conta['saldo']+= valor

def saca(conta,valor):
    conta['saldo']-= valor

def extrato(conta):
    print(f'numero: {conta["numero"]}\nsaldo: {conta["saldo"]}')

