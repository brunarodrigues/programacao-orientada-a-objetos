class  Tamagotchi:
    def __init__(self,nome="luz",fome=10,saude=10,idade=0):
        self.nome = nome
        self.fome = fome
        self.saude =saude
        self.idade =idade

    def alterar_nome(self,novo_nome):
        self.nome = novo_nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def comer(self):
        for comida in range(self.fome):
            self.fome+=1

    def tomar_injecao(self):
        for injeccao in range(self.saude):
            self.saude+=1

    def envelhecer(self):
        self.saude-=1
        self.idade+=1

    def imprimir(self):
        print(f"nome: {self.nome}\nfome: {self.fome}\nsaude: {self.retornar_saude()}\nidade: {self.idade}")

t1 = Tamagotchi()
t1.alterar_nome(input("digite um novo nome: "))
t1.retornar_fome()
t1.retornar_saude()
t1.retornar_idade()
t1.comer()
t1.tomar_injecao()
t1.envelhecer()
t1.imprimir()