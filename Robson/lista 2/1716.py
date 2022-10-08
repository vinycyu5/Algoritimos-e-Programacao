#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

codigo = input()
salario = float(input())

if codigo == "A":
    codigo1 = salario * 1.10
    print("Novo salário: R$%.2f" %(codigo1))

elif codigo == "B":
    codigo2 = salario * 1.15
    print("Novo salário: R$%.2f" %(codigo2))

elif codigo =="C":
    codigo3 = salario * 1.20
    print("Novo salário: R$%.2f" %(codigo3))