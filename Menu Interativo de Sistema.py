# =========================================================
# INSTITUIÇÃO: Colégio Estadual Jardim Oriente (CEJO) / SENAI
# CURSO: Técnico em Desenvolvimento de Sistemas
# ESTUDANTE: [Seu Nome Completo]
# TURMA: 1º A (Matutino) / 1º B (Vespertino)
# DATA: 13/10/2026
# UC: Lógica de Programação I / Programação de Apps I
# DESCRIÇÃO: Prática de Laço WHILE (Menu Interativo)
# =========================================================

opcao = -1

# O laço vai rodar enquanto a opção for diferente de 0
while opcao != 0:
    print("\n==========================================")
    print("    SISTEMA DE GESTÃO CEJO / SENAI       ")
    print("==========================================")
    print("1 - Cadastrar Novo Cliente")
    print("2 - Listar Produtos do Estoque")
    print("3 - Consultar Status do Servidor")
    print("0 - Sair do Sistema")
    
    opcao = int(input("\nDigite a opção desejada: "))
    
    if opcao == 1:
        print("\n>> [MÓDULO]: Tela de Cadastro de Cliente selecionada!")
    elif opcao == 2:
        print("\n>> [MÓDULO]: Exibindo lista de produtos em estoque...")
    elif opcao == 3:
        print("\n>> [MÓDULO]: Servidor operando 100% online.")
    elif opcao == 0:
        print("\nEncerrando o sistema... Até logo!")
    else:
        print("\n❌ Opção inválida! Tente novamente.")
