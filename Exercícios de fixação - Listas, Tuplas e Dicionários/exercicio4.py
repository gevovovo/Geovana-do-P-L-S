nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

notas = [nota1, nota2, nota3]

media_inicial = sum(notas) / len(notas)
print(f"\nLista de notas: {notas}")
print(f"Média inicial: {media_inicial:.2f}")

menor_nota = min(notas)
indice_menor = notas.index(menor_nota)

nova_nota = float(input(f"A menor nota foi {menor_nota}. Digite a nota substituta: "))
notas[indice_menor] = nova_nota
notas.sort()
nova_media = sum(notas) / len(notas)

print(f"\nLista de notas atualizada e ordenada: {notas}")
print(f"Nova média: {nova_media:.2f}")