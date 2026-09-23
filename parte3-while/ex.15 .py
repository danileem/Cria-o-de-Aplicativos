contador = 0

while True:
    numero = int(input("Digite um número, ou 0 para sair: "))

    if numero == 0:
        break
    elif numero > 0:
        contador = contador + 1

print("Quantidade de números positivos digitados foi de:", contador)