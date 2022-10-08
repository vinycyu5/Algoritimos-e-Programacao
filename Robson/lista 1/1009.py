#https://www.beecrowd.com.br/judge/pt/problems/view/1008

nomeDoVendedor = input()

salarioFixo = float(input())

vendas = float(input())

TOTAL = salarioFixo + 0.15 *vendas

print("TOTAL = R$ %.2f" %(TOTAL))