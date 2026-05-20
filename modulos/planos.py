def escolha_seu_plano():

    planos = {
        1: "Ouro",
        2: "Social",
        3: "Prata",
        4: "Bronze"
    }

    while True:

        print("\n" + "=" * 70)
        print("ESCOLHA SEU PLANO".center(70))
        print("=" * 70 + "\n")

        print(" [1] - Ouro   → 100% desconto - R$450,00/mês")
        print(" [2] - Social → 80% desconto [Consulte elegibilidade]")
        print(" [3] - Prata  → 50% desconto - R$250,00/mês")
        print(" [4] - Bronze → 20% desconto - R$89,90/mês\n")

        try:
            escolha = int(input("Escolha o plano: "))

        except ValueError:
            print("\n❌ Digite apenas números!\n")
            continue

        if escolha not in planos:
            print("\n❌ Escolha uma opção válida!\n")
            continue

        if escolha == 2 and not valida_plano_social():
            continue

        return planos[escolha]

def valida_plano_social():

    print("\n" + "=" * 40)
    print("PLANO SOCIAL".center(40))
    print("=" * 40 + "\n")

    print("📌 Exigências:\n")
    print("• Ser maior de 18 anos")
    print("• Renda máxima de R$1.621,00\n")

    print("Vamos verificar sua elegibilidade.\n")

    while True:

        try:
            renda = float(
                input("Qual o valor da sua renda mensal? ").replace(",", ".")
            )

        except ValueError:
            print("\n❌ Digite um valor válido!\n")
            continue

        if renda > 1621:
            print("\n❌ Renda superior à permitida.")
            print("Escolha outro plano.\n")

            return False

        return True