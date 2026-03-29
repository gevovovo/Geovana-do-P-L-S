nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
produto = {"nome": nome, "preco": preco}

print(f"Antes: {produto}")
produto.pop("desconto", None)

print(f"Depois: {produto}")