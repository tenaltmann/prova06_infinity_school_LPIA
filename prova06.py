
# caso queira esconder os inputs de senha com ****, basta descomentar o "import pwinput" e as variaveis comentadas por suas versoes não comentadas.
 
#import pwinput                                                                 


nome_usuario = str(input("Defina seu nome de usuário: "))                       #define o nome de usuário
senha = str(input("Defina sua senha: "))                                        #define a senha
#senha = pwinput.pwinput("Defina sua senha: ")  
tentativas = 3                                                                  #contador de tentativas


while tentativas > 0:                                                           #estrutura de repetição que permite a visualização do menu a cada tentativa

    
    print(" 1. Efetuar o login 2. Sair")                        
    opcao = int(input("Escolha uma opção: "))                                   # seleciona a opçãp do menu

    if opcao == 1:                                                              # condicional de realização do login
        for i in range(tentativas):                                             # Loop de repetição limitada ao número de tentativas

            confere_usuario = str(input("Usuário: "))                           #variavel do nome de usuário no login
            confere_senha = str(input("Senha: "))                               #variavel da senha no login
            #confere_senha = pwinput.pwinput("Senha: ")

            if confere_usuario == nome_usuario and confere_senha == senha:      #condicional que confere se todas as credenciais conferem
                print("Boas Vindas, seu Login foi efetuado com sucesso")        
                tentativas = 0                                                  #zera as tentivas encerrando o loop while e for
                break                                                           
            else:
                tentativas -= 1                                                 # diminui a tentativa e menos 1
                if tentativas >= 1:                                             # condicional que mostra o número de tentativas restante
                    print(f"Você possui mais {tentativas} tentativa(s)")
                else:       
                    for i in range(3):                                          # loop de repetição das 3 mensagens de acesso bloqueado conforme solicitado no enunciado
                        print("Acesso Bloqueado !")
                    break

    elif opcao == 2:                                                            # opção de encerrar o código
        print("Saindo...")
        break
    else:                                                                       # força o usuário a responder conforme o menu
        print("Escolha uma opção valida!")


  