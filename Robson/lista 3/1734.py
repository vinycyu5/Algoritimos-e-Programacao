#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

n = int( input())
i = int(1)
x = int(1)

while i <= n:
    x *= i
    i += 1
print("%i! = %i" %(n,x))