#Média de Notas 
nome = input("Digite o seu nome:")
nota1 = float(input("Digite a primera nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
result = media
if result >=7:
    print(f"O aluno {nome}, foi aprovado com a média de {media}.")
elif result >=3 and result <7:
    print(f"O aluno {nome}, está de recuperação com a média de {media}.")
else:
    print(f"O aluno {nome}, foi reprovado com a média de {media}.")