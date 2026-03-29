nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
aluno = {"nome": nome, "idade": idade}

print(f"Resultado do Ex 6: {aluno}")
print(f"Tipo: {type(aluno)}")

nota = float(input("Digite a nota do aluno: "))
aluno["nota"] = nota 

print(f"Resultado final (Ex 7): {aluno}")