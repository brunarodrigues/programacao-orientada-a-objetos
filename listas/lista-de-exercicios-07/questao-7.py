class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.envelhecer+=1


    def engordar(self):
        self.peso+=3


    def emagrecer(self):
        self.peso-=2

    def crescer(self):
        if (self.idade<=21):
            self.altura+=0.05
        else: 
            return self.altura

    def imprimir(self):
        print(f"nome: {self.nome}\n idade: {self.idade}\npeso: {self.peso}\naltura: {self.altura:.2f}")

p1 = Pessoa("luz",18,49,1.60)
p1.engordar()
p1.emagrecer()
p1.crescer()
p1.imprimir()