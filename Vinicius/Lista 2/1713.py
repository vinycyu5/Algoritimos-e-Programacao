#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1712

ganho_hora = float(input(""))
num_trab = float (input(""))

salario_mes = ganho_hora * num_trab
ir = salario_mes * 0.11 
inss = salario_mes * 0.08
sindicato = salario_mes * 0.05
descontos = ir + inss + sindicato 
liquido = salario_mes - descontos
 
print("Salário bruto: R${:.2f}" .format(salario_mes))
print("Imposto: R${:.2f}" .format(ir))
print("INSS: R${:.2f}" .format(inss))
print("Sindicato: R${:.2f}" .format(sindicato))
print("Líquido: R${:.2f}" .format(liquido ))