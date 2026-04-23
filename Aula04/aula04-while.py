cp = 0

while cp < 3:
    print(f"Produto {cp}")
    cp = cp + 1

#while decrescente
i = 4

while i >= 0:
    print(i)
    i -= 1

#repetição com entrada de usuario
jogar = "sim"

while jogar.lower() == "sim":
    print("Repete ou inicia jogo")
    jogar = input("Deseja jogar novamente?")

#modificadores de laço break - continue

i = 0

while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 7:
        break
    print(f"Produto{i}")

#Algoritmo que recebe um numero inteiro positivo n
#Imprime na tela todos os numeros de 1 a n

n = int(input("Digite um numero inteiro positivo n:"))

cont = 1

while cont <= n:
    print(cont)
    cont += 1

#Escreva um ´programa que dadas as duas notas de 0 a 10
#calcule a media aritmetica entre elas

def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota_temp = float(input("Digite novamente a nota:"))
    return nota_temp
#solicitar e validar a primeira nota

notaA = float(input("Digite a primeira nota:"))
while notaA < 0 or notaA > 10:
    print("A nota deve estar entre 0 e 10")
    notaA = float(input("Digite novamente a primeira nota:"))

# solicitar e validar a segunda nota

notaB = float(input("Digite a segunda nota:"))
while notaB < 0 or notaA > 10:
    print("A nota deve estar entre 0 e 10")
    notaB = float(input("Digite novamente a segunda nota:"))

#calcular a media

media = (NotaA + notaB)/2
print("A media é", media)