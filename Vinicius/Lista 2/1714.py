#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

produto = float(input (""))

lucro = 0.45 * produto
lucro2 = 0.30 * produto
if produto < 20:
    lucro_final = lucro + produto
    print("Valor de venda: R${:.2f}".format(lucro_final))
else:
    lucro_final2 = lucro2 + produto
    print("Valor de venda: R${:.2f}".format(lucro_final2))