# ==========================================
# JOGO DA ADIVINHAÇÃO DE NÚMEROS 🎯
# ==========================================

numero_secreto = 7  # Os alunos podem mudar o número aqui

print("=== JOGO DA ADIVINHAÇÃO DO CEJO ===")
jogador = input("Digite seu nome: ")
print(f"\nOlá {jogador}! Tente adivinhar o número secreto entre 1 e 10.")

chute = int(input("Qual é o seu palpite? "))

if chute == numero_secreto:
    print(f"\n🎉 PARABÉNS, {jogador}! Você acertou! O número secreto era {numero_secreto}.")
elif chute > numero_secreto:
    print(f"\n❌ Que pena! O seu chute ({chute}) foi MAIOR do que o número secreto.")
else:
    print(f"\n❌ Que pena! O seu chute ({chute}) foi MENOR do que o número secreto.")

print("\nObrigado por jogar!")
