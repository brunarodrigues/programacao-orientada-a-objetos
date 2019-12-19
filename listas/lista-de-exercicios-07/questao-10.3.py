class Chinelo:
    def __init__(self,cor,marca,modelo,tamanho):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.tamanho = tamanho
    

    def mostrar_cor(self):
        return self.cor
    def mudar_cor(self,nova_cor):
        self.cor = nova_cor

    def mostrar_marca(self):
        return self.marca
    def mudar_marca(self,nova_marca):
        self.marca = nova_marca
    def mostrar_tamanho(self):
        return self.tamanho
    def mostrar_modelo(self):
        return self.modelo
    def imprimir(self):
        print(f"cor: {self.cor}\nmarca: {self.marca}\ntamanho: {self.tamanho}\nmodelo: {self.modelo}")

c1 = Chinelo("branco","ipanema","sandália",37)    
x = c1.mostrar_cor()
print(x)
c1.mudar_cor("preto")
x = c1.mostrar_marca()
print(x)
c1.mudar_marca("havaianas")
c1.mostrar_tamanho()
c1.mostrar_modelo()
c1.imprimir()

