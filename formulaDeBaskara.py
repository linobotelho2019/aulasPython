import math

a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))

delta = b**2 - 4*a*c #para calcular o delta 
raiz = delta ** (1/2)
x1 = (-b+raiz)/(2*a)
x2 = (-b-raiz)/(2*a)

if delta < 0:
	exit("Valor menor que zero não existe raiz real")
if x1 == x2:
	exit(f'X1 e X2 são iguais, resultado x = {x1}')
if x1 != x2:
	exit(f'X1= {x1} X2= {x2}')


# FORMULA DE BASKARA ax** + bx + c = 0
# x=-b+-raiz b** -4*a*c sobre 2*a


