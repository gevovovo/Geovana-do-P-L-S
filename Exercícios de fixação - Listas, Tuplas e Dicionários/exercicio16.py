lista = []

for i in range(5):
    item = input(f"Digite o {i+1}º item da lista: ")
    lista.append(item)

print(f"\nSua lista completa: {lista}")
tres_primeiros = lista[0:3]
print(f"Os três primeiros itens são: {tres_primeiros}")

dois_ultimos = lista[-2:]
print(f"Os dois últimos itens são: {dois_ultimos}")