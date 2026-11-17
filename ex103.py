
# Apresentação
print("Programa para converter valores em moedas.")
print("")

# Entrada de dados
moedas = dict()

arquivo = open("moedas - moedas.csv", "r", encoding="utf8")

for linha in arquivo:
    partes = linha.strip().split(",")

    sigla = partes[0]
    nome = partes[2]
    cotacao = float(partes[3])

    moedas[sigla] = {
        "nome": nome,
        "cotacao": cotacao
    }

arquivo.close()

valor = float(input("Informe o valor em R$: "))
destino = input("Informe a sigla da moeda de destino: ").upper()

# Processamento
if destino in moedas:
    nome = moedas[destino]["nome"]
    cotacao = moedas[destino]["cotacao"]
    convertido = valor / cotacao

    # Saída de dados
    print("")
    print(f"Moeda: {nome}")
    print(f"Valor convertido: {convertido:.2f}")
else:
    print("Moeda não encontrada.")
