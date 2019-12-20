class Mochila:
    def __init__(self,cor,tamanho,marca,material):
        self.cor = cor
        self.tamanho= tamanho
        self.marca= marca
        self.material = material
    
    def mostrar_cor(self):
        return self.cor

    def mostrar_tamanho(self):
        return self.tamanho
    
    def mostrar_marca(self):
        return self.marca
    def mostrar_material(self):
        return self.material
    def mudar_material(self,novo_material):
        self.material = novo_material



    def imprimir(self):
        print(f"cor: {self.cor}\ntamanho: {self.tamanho}\nmarca: {self.marca}\nnovo material: {self.material}")

m1 = Mochila("preta","grande","Bottega Veneta","couro")
m1.mostrar_tamanho()
m1.mostrar_cor()
m1.mostrar_marca()
x = m1.mostrar_material()
print(x)
m1.mudar_material("nylon")

m1.imprimir()