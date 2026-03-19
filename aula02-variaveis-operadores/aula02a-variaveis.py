print("Olá Mundo")

print(7+4)
print("7+4")
print("7"+"4") #concatenando strings

#Comentário de 1 linha
#Variaveis
nome = "Leo" #str
idade = 18 #int
peso = 60 #float

print(nome, idade, peso)
print(f"Olá, {nome}!!!")

#input -- simulação de um forms no cmd
nome = input("Digite o seu nome:")
idade = int(input("Digite sua idade:"))
peso = float(input("Digite seu peso:"))

print(nome, idade, peso)
print(idade + 1)

ano_nascimento = 2008
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f'Sua idade é: {idade}')
