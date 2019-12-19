class Macaco:
    def __init__(self,nome,bucho):
        self.nome = nome
        self.bucho = bucho
    def comer(self,comida):
        self.bucho.append(comida)


    def ver_bucho(self):
        print("bucho: ",self.bucho)
    
    
    def digerir(self):
        del(self.bucho[0])

    def imprimir(self):
        print(f"nome: {self.nome}\nbucho: {self.bucho}")

m1 = Macaco("mario",["banana","abacate","mamão"])
m1.comer("plantas")
m1.ver_bucho()
m1.digerir()
m1.imprimir()

m2 = Macaco("pedro",["folhas","flores","sementes"])
m2.comer(m1)
m2.ver_bucho()
m2.digerir()
m2.imprimir()
print(type(m2))