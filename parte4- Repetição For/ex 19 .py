numero = int(input("Escolha um número: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print("O fatorial deste número é,", fatorial)