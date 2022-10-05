#https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = input("")
salario = float(input(""))
total_vendas = float(input(""))

comissao = 0.15 * total_vendas
salario_comissao = salario + comissao

print("TOTAL = R$ {:.2f}" .format(salario_comissao))