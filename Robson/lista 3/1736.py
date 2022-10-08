#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1736

quant_num = int(input(""))
acumulador = 0
contador = 0
if quant_num <= 0:
    print("Informe uma quantidade > 0!")
else:    
    while contador < quant_num:
        soma = int(input(""))
        acumulador = acumulador + soma
        contador = contador + 1
    print("Soma dos números informados: %.2f" %(acumulador))