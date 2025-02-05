import pwinput
nome_usuario = str(input("Defina seu nome de usuário"))
senha = pwinput("Defina sua senha:")
tentivas = 3


while True:

    print(" 1. Efetuar o login 2. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        for i in range(tentivas):
            confere_usuario = str(input("Usuário: "))
            confere_senha = str(input("Senha: "))
            if confere_usuario == nome_usuario and confere_senha == senha == True:
                print("Login Efetuado")

