class Bicicleta:
    def __init__(self,cor,marca,farol=True):
        self.cor = cor
        self.marca = marca
        self.farol = farol
        

    def retornar_cor(self):
        return self.cor
    
    def mudar_cor(self,nova_cor):
        self.cor = nova_cor

    def mostrar_marca(self):
        return self.marca

    def ligar_farol(self):
        if(self.ligar_farol==True):
            return "farol ligado(NOITE)"
        else:
            return "farol desligado(DIA)"

    def imprimir(self):
        print(f"cor: {self.cor}\nmarca: {self.marca}")

b1 = Bicicleta("rosa","Caloi Strada Racing")
r = b1.retornar_cor()
print(r)
b1.mudar_cor("amarelo")
b1.mostrar_marca()

b1.imprimir()
l = b1.ligar_farol()
print(l)