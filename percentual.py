estados_lista = [("rj", "36678.66"), ("sp", "67836.43"), ("mg", "29229.88"), ("es", "27165.48"), ("outros", "19849.53")]

estados = dict(estados_lista)


total = sum(float(valor) for chave, valor in estados.items())
print(f"O total faturado é {str(total)}")

for chave, valor in estados.items():
    faturamento = float(valor)
    represent = faturamento / total * 100

    print(f" {chave} tem o faturamento {faturamento} e a represtatividade é {round(represent, 2)}%")
