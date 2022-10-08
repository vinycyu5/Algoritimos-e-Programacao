#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1735

contadorinicial = int(input())
contadorfinal = int(input())

while contadorinicial >= contadorfinal:
    contador = contadorinicial + 1
    print("%i" %(contadorinicial))
    contadorinicial -= 1
print("FOGO!")