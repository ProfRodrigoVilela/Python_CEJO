opcao = -1

# Laço WHILE principal que mantém o menu ativo
while opcao != 0:
    print("\n==========================================")
    print("   SISTEMA DE PRÁTICA: WHILE E FOR        ")
    print("==========================================")
    print("1 - Testar Estrutura WHILE (Contagem Regressiva)")
    print("2 - Testar Estrutura FOR (Gerador de Tabuada)")
    print("0 - Sair do Sistema")
    
    opcao = int(input("\nEscolha uma opção: "))
    
    # OPÇÃO 1: Exemplo prático de WHILE
    if opcao == 1:
        print("\n--- [DEMO WHILE]: Contagem Regressiva ---")
        inicio = int(input("Digite um número inteiro para iniciar: "))
        
        while inicio >= 0:
            print(f"Contagem: {inicio}")
            inicio = inicio - 1  # Decremento
            
        print("🚀 Fim da contagem!")
        
    # OPÇÃO 2: Exemplo prático de FOR
    elif opcao == 2:
        print("\n--- [DEMO FOR]: Gerador de Tabuada ---")
        num = int(input("Digite o número da tabuada desejada: "))
        
        print(f"\nTabuada do {num}:")
        for i in range(1, 11):
            print(f"{num} x {i:2d} = {num * i}")
            
        print("✨ Tabuada gerada com sucesso!")
        
    # OPÇÃO 0: Encerramento
    elif opcao == 0:
        print("\nEncerrando o programa... Até logo!")
        
    else:
        print("\n❌ Opção inválida! Tente novamente.")
