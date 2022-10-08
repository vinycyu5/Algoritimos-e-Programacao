#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = input()
hrx = float(input())

salMinimo = 1192.40
valorHrx = 10.00

salHrx = hrx * valorHrx
salBruto = 3 * salMinimo + salHrx

if salBruto > 2000.00:
    inss = salBruto * 0.12
    if salBruto >= 2500.00:
     ir = salBruto * 0.20
elif salBruto < 2000.00:
    inss = salBruto * 0.05


salarioLiquido = salBruto - (inss + ir)
print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %(salBruto))
print("Salário líquido: R$%.2f" %(salarioLiquido))