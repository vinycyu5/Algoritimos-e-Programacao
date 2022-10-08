#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1712

valor_hr = float(input())
numeroDeHr = float(input())

salarioBruto = valor_hr * numeroDeHr
imposto = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
descontos = imposto + inss + sindicato
liquido = salarioBruto - descontos

print("Salário bruto: R$%.2f" %(salarioBruto))
print("Imposto: R$%.2f" %(imposto))
print("INSS: R$%.2f" %(inss))
print("Sindicato: R$%.2f" %(sindicato))
print("Líquido: R$%.2f" %(liquido))