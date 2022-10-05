#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = str(input(""))
horas_extras = float(input(""))

salario_minimo = 1192.40
val_hora_extra = 10.00

salario_hora_extra = horas_extras * val_hora_extra
salario_bruto = 3*salario_minimo + salario_hora_extra

if salario_bruto > 2000.00:
    inss = salario_bruto * 0.12
else:
    salario_bruto * 0.05
if salario_bruto > 2500.00:
    ir = salario_bruto * 0.20
        
descontos = inss + ir
salario_liquido = salario_bruto - descontos
print("Nome: {}".format(nome))
print("Salário bruto: R${:.2f}".format(salario_bruto))
print("Salário líquido: R${:.2f}".format(salario_liquido))