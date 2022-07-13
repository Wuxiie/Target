palavra = input("digite a palavra ")
palavra_invertida = ""

for c in range(len(palavra)):
    palavra_invertida = palavra_invertida + palavra[(len(palavra)-1) - c]

    print(palavra_invertida)