ganho_por_hora = float(input('Digite quanto você por hora:'))
numero_horas_trabalhadas_no_mes = float(input('Digite o número de horas trabalhadas no mês:'))
salario_bruto = ganho_por_hora*numero_horas_trabalhadas_no_mes
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto-ir-inss-sindicato

print('Salário bruto:{:.2f}'.format(salario_bruto))
print('INSS:{:.2f}'.format(inss))
print('imposto de renda:{:.2f}'.format(ir))
print('Sindicato:{:.2f}'.format(sindicato))
print('Salário liquido:{:.2f}'.format(salario_liquido))