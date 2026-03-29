fruta1 = input("Digite a 1ª fruta: ")
fruta2 = input("Digite a 2ª fruta: ")
fruta3 = input("Digite a 3ª fruta: ")

cesta_frutas = (fruta1, fruta2, fruta3)
busca = input("Qual fruta você quer verificar se está na tupla? ")

if busca in cesta_frutas:
    print(f"Sim, a fruta '{busca}' está na tupla!")
else:
    print(f"Não, a fruta '{busca}' não foi encontrada.")