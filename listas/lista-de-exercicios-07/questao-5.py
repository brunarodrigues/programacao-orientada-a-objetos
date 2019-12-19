class Pokemon:
    def __init__(self,nome,tipo,descricao,ataques,nivel=0,poder_luta=0,brilhante=True):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.ataques = ataques
        self.nivel = nivel
        self.poder_luta = poder_luta
        self.brilhante = brilhante
 
    def mostrar_ataques(self):
        print(self.ataques)
 
 
    def subir_nivel(self):
        self.nivel+=1
        self.poder_luta+=1
           
    def mostrar_poder_luta(self):
        print(self.poder_luta)
 
    def e_brilhante(self):
        if(self.brilhante==True):
            print("brilhante")
        else:
            print("não é brilhante")
    
    def adicionar_ataque(self,novo_ataque):
        self.ataques.append(novo_ataque)
    
    def imprimir(self):
        print(f"nome: {self.nome}\ntipo: {self.tipo}\ndescricao: {self.descricao}\nataques: {self.ataques}\nnivel: {self.nivel}\npoder luta: {self.poder_luta}\n")
p1= Pokemon("digimon","aço","resistente",["asa de aço"],3,6)
p1.mostrar_ataques()
p1.subir_nivel()
p1.mostrar_poder_luta()
p1.e_brilhante()
p1.adicionar_ataque("contra-ataque")
p1.imprimir()