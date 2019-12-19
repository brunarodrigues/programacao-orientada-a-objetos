class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

#trocarCor e mudarCor
    def trocar_Cor(self, novacor):
        self.cor=novacor
    def mostrar_Cor(self):
        print(self.cor)

    def imprimir(self):
        print(f"{self.cor},{self.circunferencia},{self.material}")

b1 = Bola("pink",3,"plastico")
b1.trocar_Cor("roxo")

b1.imprimir()

