import random
def embaralha(palavra):
    emb = list(palavra)
   
    emb = ''.join(random.sample(palavra, len(palavra)))
    return emb

x = embaralha(input('digite uma palavra: '))
print (x)