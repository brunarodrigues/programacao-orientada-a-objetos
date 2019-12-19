class Caneta:
    def __init__(self,cor,marca,numero_ponta,volume_tinta):
        self.cor = cor
        self.marca = marca
        self.numero_ponta = numero_ponta
        self.volume_tinta = volume_tinta
 
 
    def encher_caneta(self):
         self.volume_tinta = 50
        
 
 
    def escrever(self,palavra):
        print(palavra)
        self.volume_tinta-=1
 
 
    def retornar_marca(self):
        return self.marca
 
    def imprimir_caracteristica(self):
        print(f"{self.cor},{self.marca},{self.numero_ponta},{self.volume_tinta}")
 
c1 = Caneta("Azul","bic",0.5,50)
c1.escrever("A melhor maneira de prever o futuro é inventá-lo")
c1.imprimir_caracteristica()
