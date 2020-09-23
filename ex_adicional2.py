import math

a = float(input("Digite um valor para a "))
b = float(input("Digite um valor para b "))
c = float(input("Digite um valor para c "))

delta = (b*b)-(4*a*c)

if delta < 0:
 print("esta equação não possui raízes reais")
elif delta == 0:
 raiz1 = ((-1*b)+math.sqrt(delta))/(2*a)
 print("a raiz desta equação é", raiz1)
else:
 raiz1 = ((-1*b)+math.sqrt(delta))/(2*a)
 raiz2 = ((-1*b)-math.sqrt(delta))/(2*a)
 if raiz1<raiz2:
  print("as raízes da equação são", raiz1,"e",raiz2)
 else:
  print("as raízes da equação são", raiz2,"e",raiz1)