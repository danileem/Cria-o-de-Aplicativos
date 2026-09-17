contador = int (input("Digite um número: "))
opcao = contador

while opcao != 0:
    opcao = int(input("Digite um número ou 0 para sair: "))
    contador = contador + opcao
print("A soma é igual a:", contador)

