agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}
novo_nome = input("Digite o nome do novo contacto: ")
novo_tel = input("Digite o telefone: ")
agenda[novo_nome] = novo_tel

nome_busca = input("Digite o nome para atualizar o telefone: ")
if nome_busca in agenda:
    novo_tel_atualizado = input("Digite o novo telefone: ")
    agenda[nome_busca] = novo_tel_atualizado
else:
    print("Contacto não encontrado para atualização.")

nome_remover = input("Digite o nome do contacto a remover: ")
if nome_remover in agenda:
    agenda.pop(nome_remover)
    print(f"Contacto {nome_remover} removido.")
else:
    print("Contacto não existe na agenda.")

nomes_ordenados = sorted(agenda.keys())

print("\n--- Agenda Ordenada ---")
for nome in nomes_ordenados:
    print(f"Nome: {nome} | Telefone: {agenda[nome]}")