senha_correta = "senai123"
opcao =  (input("Digite a senha correta: "))



while opcao != senha_correta:
    opcao = input("Senha errada, tente novamente: ")

print("Senha correta!")
