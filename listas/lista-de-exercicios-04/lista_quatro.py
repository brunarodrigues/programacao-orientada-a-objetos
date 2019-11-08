with open('amazon.csv') as arquivo:

 
	primeira_questao = 0
	segunda_questao = 0
	terceira_questao = 0
	quarta_questao = 0
 
	for linha in arquivos:
		linha = linha.strip(' ')
		ano,cidade,numeros_de_casos,data = linha.split(',')
		casos = casos.replace('.','')
 
 
	if '"Acre"' == cidade and ano == '2015':
		primeira_questao +=  int(numeros_de_casos)
 
 	elif '"Ceara"' == cidade and ano == '2014':
		segunda_questao +=  int(numeros_de_casos)
 
 
	elif '"Amazonas"' == cidade:
		terceira_questao +=  int(numeros_de_casos)
 
 
 
	if ano == '"year"':
		continue
 	elif int(ano) >= 2010 and cidade == '"Mato Grosso"':
		quarta_questao += int(numeros_de_casos)
 
 
 
print ('Questão 1: '.format(primeira_questao))
print ('Questão 2: '.format(segunda_questao))
print('Questão 3: '.format(terceira_questao))
print('Questão 4: '.format(quarta_questao))
if arquivo.closed:
	print('Arquivo está fechado')

