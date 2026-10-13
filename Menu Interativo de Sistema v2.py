# =========================================================
# INSTITUIÇÃO: Colégio Estadual Jardim Oriente (CEJO) / SENAI
# CURSO: Técnico em Desenvolvimento de Sistemas
# ESTUDANTE: Rodrigo Vilela
# TURMA: 1º A (Matutino) / 1º B (Vespertino)
# DATA: 13/10/2026
# UC: Lógica de Programação I / Programação de Apps I
# DESCRIÇÃO: Prática de Laço WHILE (Menu Interativo com Cadastro)
# =========================================================
# pelo menos uma vez (pois -1 é diferente de 0).
opcao = -1
lista_clientes = []

# O laço vai rodar enquanto a opção for diferente de 0
while opcao != 0:

    # Exibe o menu na tela
    print("\n==========================================")
    print("    SISTEMA DE GESTÃO CEJO / SENAI       ")
    print("==========================================")
    print("1 - Cadastrar Novo Cliente")
    print("2 - Listar Clientes Cadastrados")
    print("3 - Consultar Status do Servidor")
    print("0 - Sair do Sistema")

    # Lemos a resposta como TEXTO primeiro (sem converter com int).
    entrada = input("\nDigite a opção desejada: ")

    # .strip() remove espaços em branco antes e depois do texto
    # .isdigit() verifica se o texto contém SOMENTE números
    if entrada.strip().isdigit():
        # Só convertemos para inteiro quando temos certeza que é número
        opcao = int(entrada)
    else:
        opcao = -1
 
    # OPÇÃO 1: CADASTRAR CLIENTE
    if opcao == 1:
        print("\n>> [MÓDULO]: Tela de Cadastro de Cliente")
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

    elif opcao == 2:
        print("\n>> [MÓDULO]: Lista de Clientes Cadastrados")

        # len() conta quantos itens existem na lista
        if len(lista_clientes) == 0:
            print("⚠️ Nenhum cliente cadastrado ainda.")
        else:
            print(f"Total de clientes: {len(lista_clientes)}\n")
            for indice, cliente in enumerate(lista_clientes):
                print(f"{indice + 1}. {cliente}")

    elif opcao == 3:
        print("\n>> [MÓDULO]: Servidor operando 100% online.")
    elif opcao == 0:
        print("\nEncerrando o sistema... Até logo!")
    # QUALQUER OUTRO VALOR: OPÇÃO INVÁLIDA
    else:
        print("\n❌ Opção inválida! Digite apenas 0, 1, 2 ou 3.")

# Fim do programa
