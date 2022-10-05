#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

fatorial = int(input())
contador = 1
resultado = 1
while contador <= fatorial:
    resultado = resultado * contador
    contador = contador +1
print("{}! = {}".format(fatorial, resultado))