class Pente:
    def __init__(self,cor,tamanho):
        self.cor = cor
        self.tamanho = tamanho
    def mostrar_cor(self):
        print(self.cor)

    def mudar_cor(self,nova_cor):
        self.cor = nova_cor
    def tamanho_pente(self):
        print(self.tamanho)
    def mudar_tamanho_Pente(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def imprimir(self):
        print(f"cor: {self.cor}\ntamanho: {self.tamanho}")

p1 = Pente("verde","grande")
p1.mostrar_cor()
p1.mudar_cor("azul")
p1.tamanho_pente()
p1.mudar_tamanho_Pente("pequeno")

p1.imprimir()