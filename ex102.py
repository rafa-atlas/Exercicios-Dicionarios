# Apresentação
print("Programa para separar pessoas por idade.")
print("")

# Entrada de dados
pessoas = list()

for i in range(10):
    nome = input(f"Informe o nome da {i + 1}ª pessoa: ")
    idade = int(input(f"Informe a idade de {nome}: "))

    pessoa = {
        "nome": nome,
        "idade": idade
    }

    pessoas.append(pessoa)

# Processamento
menores = list()
maiores = list()

for pessoa in pessoas:
    if pessoa["idade"] < 18:
        menores.append(pessoa)
    else:
        maiores.append(pessoa)

# Saída de dados
print("")
print("Pessoas com menos de 18 anos:")
for pessoa in menores:
    print(f"Nome: {pessoa['nome']} - Idade: {pessoa['idade']}")

print("")
print("Pessoas com 18 anos ou mais:")
for pessoa in maiores:
    print(f"Nome: {pessoa['nome']} - Idade: {pessoa['idade']}")
