fila = ["Ana", "Bruno"]

novos = [input("Novo cliente 1: "), input("Novo cliente 2: ")]
fila.extend(novos)
print(f"Fila após chegadas: {fila}")

prioritario = input("Nome do prioritário: ")
fila.insert(1, prioritario)
print(f"Fila com prioridade: {fila}")

atendido = fila.pop(0)
print(f"Atendendo agora: {atendido}")
print(f"Fila restante: {fila}")