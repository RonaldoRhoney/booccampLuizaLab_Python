# Leitura da entrada: preço e código de promoção
entrada = input().strip()
preco_str, codigo_promocao = entrada.split()

# Conversão do preço para float
preco = float(preco_str)

# Verifica se o produto está em promoção
if codigo_promocao == "S":
    preco_final = preco * 0.9  # aplica 10% de desconto
else:
    preco_final = preco  # mantém o preço original

# Exibe o valor final com duas casas decimais
print(f"{preco_final:.2f}")