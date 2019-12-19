
"""Crie uma classe que modele um retângulo:
Atributos: lado_a, lado_b

 (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: mudar_valor_lado, retornar_valor_lado, calcular_area e calcular_perimetro

Crie um programa que utilize esta classe.
 Ele deve pedir ao usuário que informe as medidas de um local.
  Depois, deve criar um objeto com as medidas e calcular
   quantos metros quadrados de pisos e quantos metros de rodapés serão necessários para o local.
"""

class Retangulo:
    def __init__(self,lado_a,lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
    
    def mudar_valor_lado(self,novo_lado):
        self.lado_a = novo_lado
        self.lado_b = novo_lado


    def retornar_valor_lado(self):
        return self.lado_a
        return self.lado_b

    def calcular_area(self):
        return self.lado_a*self.lado_b


    def calcular_perimetro(self):
        return self.lado_a*2+(self.lado_b*2)

    def imprimir(self):
        print(f"piso: {self.calcular_area()}\nrodapé: {self.calcular_perimetro()}")


retangulo_lado_a = int(input("digite tamanho do lado: "))
retangulo_lado_b = int(input("digite o tamanho do lado b: "))
r1 = Retangulo(retangulo_lado_a,retangulo_lado_b)



r1.imprimir()