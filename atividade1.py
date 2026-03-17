frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4]

print("Primeira fruta: ", frutas [0])
print("última fruta: ", frutas [-1])

frutas[1] = "banana-nanica"
print("Após alterar: ", frutas)

frutas.append("morango")
frutas.insert(1, "pera")
print("Após adicionar: ", frutas)

frutas.remove("uva")
ultima = frutas.pop()

print("Após remover 'uva' e pop(): ", frutas, "|Última removida: ", ultima)

print("Tamanho da lista 'frutas': ",len(frutas))

print("Fatiamento [0:2]: ", frutas[0:2])

print("Tem 'maçã'?", "maçã" in frutas)

print("Lista original 'numeros': ", numeros)
print("Soma dos números: ", sum (numeros))
print("Maior número: ", max(numeros))
print("Menor número: ", min(numeros))
numeros.reverse()
print("Ordenada crescente: ", numeros)
numeros.sort(reverse=True)
print("Menor número: ", numeros)

for fruta in frutas:
    print("Fruta: ", fruta)

quadrados = [n * n for n in [1, 2, 3, 4, 5]]
print("Quadrados: ", quadrados)