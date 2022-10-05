#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

codigo = int(input(""))
compra = float(input(""))
desc_func = 0.13 * compra
desc_pre = 0.07 * compra

if codigo == 1:
    comun = compra
    print("Valor total a ser pago: R${:.2f}".format(comun))

elif codigo == 2:
    funcionario = compra - desc_func
    print("Valor total a ser pago: R${:.2f}".format(funcionario))

elif codigo == 3:
    premium = compra - desc_pre
    print("Valor total a ser pago: R${:.2f}".format(premium))

else:
    print("OPÇÃO INVÁLIDA!")