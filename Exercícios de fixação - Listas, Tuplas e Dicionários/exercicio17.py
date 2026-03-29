num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))
num4 = int(input("Digite o 4º número: "))

numeros = (num1, num2, num3, num4)

print(f"\nSua tupla é: {numeros}")
print(f"A soma de todos: {sum(numeros)}")
print(f"O maior valor: {max(numeros)}")
print(f"O menor valor: {min(numeros)}")
print(f"A média aritmética: {sum(numeros) / len(numeros)}")