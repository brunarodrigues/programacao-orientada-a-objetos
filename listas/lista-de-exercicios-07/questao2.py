class Computador:
    lista = []
    
    def __init__(self,marca,modelos,componentes,anos_uso,cor):
        self.marca = marca
        self.modelos = modelos
        self.componentes = componentes
        self.anos_uso = anos_uso
        self.cor = cor
    

    def mostrar_marca(self,nova_marca):
        self.marca = nova_marca
    def adicionar_componentes(self,novos_componentes):
        self.componentes.append(novos_componentes)
        
    def mostrar_componentes(self):
        print(self.componentes)
    def mostrar_anos_uso(self):
        
        if (self.anos_uso <6):
            print(self.anos_uso)
        else:
            print("Seu computador está tão velho que tem problemas de junta… junta tudo e joga fora...")
    def envelhecer(self):
        self.anos_uso+=1
    
    def imprimir(self):
        print(f"{self.marca},{self.modelos},{self.componentes},{self.anos_uso},{self.cor}")

c1 = Computador("positivo","padrao",["mouse","teclado"], 4,"preto")
c1.adicionar_componentes("monitor,placa de video")
c1.mostrar_anos_uso()
c1.imprimir()