nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço: "))
quantidade = int(input("Digite a quantidade: "))

produto = {
    "nome": nome, 
    "preco": preco, 
    "quantidade": quantidade
}

percentual = float(input("Digite a porcentagem de aumento (ex: 10 para 10%): "))
produto["preco"] = produto["preco"] * (1 + percentual / 100)
produto["quantidade"] = produto["quantidade"] + 2

total = produto["preco"] * produto["quantidade"]

print(f"Dicionário atualizado: {produto}")
print(f"Valor total em estoque: R$ {total:.2f}")