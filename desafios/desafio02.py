# Lê a linha de entrada e separa os produtos em uma lista
produtos = input().strip().split()

# Inicializa variáveis
mais_frequente = None
maior_contagem = 0

# Percorre cada produto da lista
for i in range(len(produtos)):
    produto_atual = produtos[i]
    contagem = 0

    # Conta quantas vezes esse produto aparece
    for j in range(len(produtos)):
        if produtos[j] == produto_atual:
            contagem += 1

    # Atualiza o mais frequente (mantém o primeiro em caso de empate)
    if contagem > maior_contagem:
        maior_contagem = contagem
        mais_frequente = produto_atual

# Imprime o resultado
print(mais_frequente)