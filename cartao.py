meuCartão = int(input("Digite o número do seu cartão de crédito: "))

cartãoLido = 1
encontreiMeuCartãoNaLista = False

while cartãoLido != 0 and not encontreiMeuCartãoNaLista:
    cartãoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartãoLido == meuCartão:
        encontreiMeuCartãoNaLista = True

if encontreiMeuCartãoNaLista:
    print("legal, meu cartão esta na lista!")
else:    
    print("eita, meu cartão não esta na lista!")