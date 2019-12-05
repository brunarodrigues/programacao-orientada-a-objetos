from random import randint

numero = int(input('digite um numero: '))
lista_nomes = ['maria','ana','luana','cristiane','joao','pedro','jose','leonardo','enzo','gabriel','leticia','carmen','yasmin','gustavo','victor','vaux','rachel','bia','laise','sara']
lista_sobrenome = ['amorim','rodrigues','sousa','paz','barbosa','figueiredo','batista','pereira','moreira','coutinho','santos','diogenes','lima','costa','almeida','nascimento','carvalho','araujo','peixoto','dantas']
with open('pessoas.txt','w') as arquivo:
    for nomes in range(0,numero):
        
        name = randint(0,len(lista_nomes)-1)
        sobrenome = randint(0,len(lista_sobrenome)-1)
        idade = randint(0,101)
        print('nome : {} {} .Idade: {}'.format(lista_nomes[name],lista_sobrenome[sobrenome],idade),file=arquivo)

         
        



