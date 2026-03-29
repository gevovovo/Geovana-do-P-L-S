n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

numeros = (n1, n2, n3, n4)
alvo = int(input("Qual número deseja contar na tupla? "))
quantidade = numeros.count(alvo)

print(f"O número {alvo} aparece {quantidade} vez(es) na tupla.")