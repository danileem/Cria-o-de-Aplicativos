Vnumeros = (1, 2, 3, 4, 5 ,6 ,7 ,8, 10, 11, 12)

for i in Vnumeros:
    print(Vnumeros)

somaT = 0
Mnumero = Vnumeros[0]
for i in Vnumeros:   
    print(i)


    somaT += i

    if i > Mnumero:

        Mnumero = i

print("Todos os números somados são: ",somaT)
print ("O maior número é: ", Mnumero)