class Moto:
    def __init__(self,cor,marca):
        self.cor = cor
        self.marca = marca



    def retornar_cor(self):
        return self.cor


    def mudar_cor(self,nova_cor):
        self.cor = nova_cor
    
    def retornar_marca(self):
        return self.marca


    def imprimir(self):
        print(f"cor: {self.cor}\nmarca: {self.marca}")

m1 = Moto("preta","honda")

r = m1.retornar_cor()
print(r)
m1.mudar_cor("azul")
m1.retornar_marca()
m1.imprimir()

