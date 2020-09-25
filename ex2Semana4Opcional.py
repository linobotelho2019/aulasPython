'''
Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".
'''
num=int(input('digite um numero: '))
num1=num
rest1=num%10
while num//10!=0:
    num=num//10
    rest=num%10
    if rest==rest1:
        print('sim')
        num=num1
        break
        rest1=rest
    if num//10==0:
        print('nao')