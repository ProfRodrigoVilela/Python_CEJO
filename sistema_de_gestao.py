# =========================================================
# INSTITUIÇÃO: Colégio Estadual Jardim Oriente (CEJO) / SENAI
# CURSO: Técnico em Desenvolvimento de Sistemas
# ESTUDANTE: Rodrigo Vilela
# TURMA: 1º A (Matutino) / 1º B (Vespertino)
# DATA: 13/10/2026
# UC: Lógica de Programação I / Programação de Apps I
# DESCRIÇÃO: Prática de Laço WHILE (Menu Interativo com Cadastro)
# =========================================================

opcao = -1
lista_clientes = []

while opcao != 0:
    # Exibir o menu na tela
    print("\n================================")
    print("    SISTEMA DE GESTÃO CEJO / SENAI    ")
    print("=================================")
    print("1 - Cadastrar | Novo cliente")
    print("2 - Listar | Clientes cadastrados")
    print("3 - Consultar |  Status do servidor")
    print("0 - Sair do sistema")

    entrada = input("\nDigite a opção desejada: ")

    if entrada.strip().isdigit():
        opcao = int(entrada)
    else:
        opcao = -1
    # OPÇÃO 1: CADASTRAR CLIENTE
    if opcao == 1:
        print("\n>>[MÓDULO]: Tela de cadastro de cliente")
        
     # Recebe o nome e já remove espaços extras das pontas
        nome_cliente = input("Digite o nome do cliente: ").strip()
        
      # Impede cadastrar um nome vazio (só Enter ou só espaços)
        if nome_cliente == "":
            print("⚠️ O nome não pode ficar em branco. Cadastro cancelado.")
        else:
            # O comando .append() adiciona o novo nome ao final da lista
            lista_clientes.append(nome_cliente)
            print(f"✅ Cliente '{nome_cliente}' cadastrado com sucesso!")
     # OPÇÃO 2: LISTAR CLIENTES
    elif opcao == 2:
        print("\n>> [MÓDULO]: Lista de Clientes Cadastrados")

        # len() conta quantos itens existem na lista
        if len(lista_clientes) == 0:
            print("⚠️ Nenhum cliente cadastrado ainda.")
        else:
            print(f"Total de clientes: {len(lista_clientes)}\n")

        for indice, cliente in enumerate(lista_clientes):
                print(f"{indice + 1}. {cliente}")

    # OPÇÃO 3: STATUS DO SERVIDOR (simulação)
    elif opcao == 3:
        print("\n>> [MÓDULO]: Servidor operando 100% online.")

    # OPÇÃO 0: SAIR
    elif opcao == 0:
        # Como opcao agora vale 0, a condição do while fica falsa
        # e o laço termina depois desta volta
        print("\nEncerrando o sistema... Até logo!")

    # QUALQUER OUTRO VALOR: OPÇÃO INVÁLIDA
    else:
        print("\n❌ Opção inválida! Digite apenas 0, 1, 2 ou 3.")
# Fim do programa

              
              

        
            

            
    
    


    





