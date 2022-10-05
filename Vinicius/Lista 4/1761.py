#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

acum = 0
i = 1

while i != 0:
    valor = float(input(""))
    acum = acum + valor
    i = i + 1
    if valor == 0:
        troco = float(input(""))
        resto = troco - acum
        break
    
print("Total da compra: R${:.2f}".format(acum))
print("Valor pago: R${:.2f}".format(troco))
print("Troco: R${:.2f}".format(resto))