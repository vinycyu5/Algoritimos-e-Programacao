#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

codigo = int(input())
valor = float(input())

if codigo == 1:
    valor1 = valor
    print("Valor total a ser pago: R$%.2f" %(valor1))
elif codigo == 2:
    valor2 = valor * 0.87
    print("Valor total a ser pago: R$%.2f" %(valor2))
elif codigo ==3:
    valor3 = valor * 0.93
    print("Valor total a ser pago: R$%.2f" %(valor3))
else:
    print("OPÇÃO INVÁLIDA!")
    valor = 0