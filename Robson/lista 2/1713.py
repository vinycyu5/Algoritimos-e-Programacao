#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valorDaCompra = float(input())

if valorDaCompra < 20:
    valorDeVenda = valorDaCompra * 1.45
    
else:
    valorDeVenda = valorDaCompra * 1.30
    
print("Valor de venda: R$%.2f" %(valorDeVenda))