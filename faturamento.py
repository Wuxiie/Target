import json

arquivo_json = open("arquivos/dados.json")
dados = json.load(arquivo_json)

dias_uteis = 0
valor_total = 0
minimo = 0
maximo = 0
for elemento in dados:
    if elemento['valor'] != 0:
        dias_uteis += 1
        valor_total += elemento['valor']
        if elemento['valor'] > maximo:
            maximo = elemento['valor']
        if elemento['valor'] < minimo or minimo == 0:
            minimo = elemento['valor']

media = valor_total / dias_uteis

num_dias = 0
for elemento in dados:
    if elemento['valor'] > media:
        num_dias += 1


print(f"O maior valor de faturamento no mês é: {round(maximo, 2)}")
print(f"o menor valor de faturamento no mês é: {round(minimo, 2)}")
print(f"O número de dias do mês em que o valor de faturamento foi superior à média mensal é: {num_dias}")
    
