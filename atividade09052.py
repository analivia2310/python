vetores= []

for i in range(10):
    num = int(input("Digite um número: "))
    vetores.append(num)

repetidos = []
for i in range(len(vetores)):
    if vetores.count(vetores[i]) > 1 and vetores[i] not in repetidos:
        repetidos.append(vetores[i])
        posicoes = []
        for j in range(len(vetores)):
            if vetores[j] == vetores[i]:
                posicoes.append(j)
        print(f"O número {vetores[i]} se repete nas posições:{posicoes}")