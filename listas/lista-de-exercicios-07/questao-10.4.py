class Radio:
    def __init__(self,cor,tipo):
        self.cor = cor
        self.tipo = tipo

    def mostrar_cor(self):
        return self.cor

    def mostrar_tipo(self):
        return self.tipo
    def mudar_tipo(self,novo_tipo):
        self.tipo = novo_tipo

    def imprimir(self):
        print(f"cor: {self.cor}\nnovo tipo: {self.tipo}")

r1 = Radio("vermelho", "AM")
r1.mostrar_cor()

x = r1.mostrar_tipo()
print("tipo: ",x)

r1.mudar_tipo("FM")
r1.imprimir()