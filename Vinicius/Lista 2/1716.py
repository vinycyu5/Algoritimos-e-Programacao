#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

codigo = (input(""))
salario = float(input(""))

A = 0.10 * salario
B = 0.15 * salario
C = 0.20 * salario

if codigo == 'A':
    novo_salario = A + salario
    print("Novo salário: R${:.2f}" .format(novo_salario))
elif codigo =='B':
    novo_salario = B + salario
    print("Novo salário: R${:.2f}" .format(novo_salario))
elif codigo == 'C':
    novo_salario = C + salario
    print("Novo salário: R${:.2f}" .format(novo_salario))