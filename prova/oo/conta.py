import datetime
class Conta:

    def __init__(self,numero,titular, saldo, limite,data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite =limite
        self.data_abertura = data_abertura
        self.historico = Historico()

    def deposita(self,valor):
        self.saldo += valor
        self.historico.transacoes.append(f'DEPOSITO DE: {valor}')
    def saca(self,valor):
        if(self.saldo< valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'SAQUE DE: {valor}')



    def extrato(self,dados):
        print(f'data de abertura : {self.data_abertura}\nconta : {self.numero}\nsaldo: {self.saldo}')
        print(dados)
        self.historico.transacoes.append(f'TIROU EXTRATO - SALDO: {self.saldo}')
    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f'TRANSFERENCIA DE : {valor} PARA CONTA: {destino.numero}')
            return True

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def __str__(self):
        return f'nome: {self.nome} {self.sobrenome}\ncpf: {self.cpf}'

class Data:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}' 

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f'DATA ABERTURA: {self.data_abertura}')
        print("TRANSAÇÕES: ")
        for t in self.transacoes:
            print("-", t)
    

def main():
    cliente1 = Cliente('jose', 'fernandes','333333333-00')
    cliente2 = Cliente('yasmin','garcia', '222222222-00')
    data = Data('28','02','2020')
    conta= Conta('123-4', cliente1.nome, 200.0, 1000.0,data)
    conta2 = Conta('124-9', cliente2.nome, 300.0, 2000.0,data)
    conta.deposita(20)
    conta.extrato(cliente1)
    conta2.saca(15)
    conta2.extrato(cliente2)
    conta.transfere_para(conta2,30)
    conta.historico.imprime()

if __name__ == '__main__':
    main()
    


