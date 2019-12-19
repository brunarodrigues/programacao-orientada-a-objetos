class Quadrado:
    def __init__(self,tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mudar_valor_lado(self, novo_lado):
        self.tamanho_do_lado = novo_lado

    def retornar_valor_lado(self):
        return self.tamanho_do_lado

    def calcular_area(self):
        area = self.tamanho_do_lado*self.tamanho_do_lado
    def imprimir(self):
        print(f"Tamanho do lado {self.tamanho_do_lado}")

q1 = Quadrado(6)
q1.mudar_valor_lado(4)
q1.retornar_valor_lado()
q1.calcular_area()
q1.imprimir()