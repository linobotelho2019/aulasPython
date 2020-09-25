'''
Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.Para saída, siga o formato do exemplo abaixo.
'''
def main ():
    n = int(input("Digite um numero: "))
    i = 0
    imp = 1
    while i < n:
        print(imp)
        i = i + 1
        imp  = imp + 2
main()