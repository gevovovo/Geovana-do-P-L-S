n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
lista = [n1, n2, n3, n4]

print(f"Tamanho antes: {len(lista)}")
alvo = int(input("Qual número deseja remover? "))

if alvo in lista:
    lista.remove(alvo)
    print("Número removido com sucesso.")
else:
    print("O número não está na lista.")

print(f"Tamanho depois: {len(lista)}")