
def fib_Vetor():
    fib = [0, 1]
    numero_Informado = int(input("Digite um número "))
    while True:
        fib_Valores = fib[-1] + fib[-2]
        fib.append(fib_Valores)
        print(fib)

        if fib_Valores == numero_Informado:
            print("o numero informado está presente na sequência de fibonacci ")
            break
        elif(fib_Valores > numero_Informado):
            print("o numero informado NÂO está presente na sequência de fibonacci ")
            break
fib_Vetor()       

        
