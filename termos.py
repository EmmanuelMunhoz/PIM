def termo_lgpd():
    while True:
        print("\n" + "=" * 70)
        print("\033[1;34m📋 TERMOS LGPD\033[0m".center(70))
        print("=" * 70)

        print("\nAntes de prosseguir com o cadastro,")
        print("precisamos do seu consentimento para uso dos dados.\n")

        print("📌 Seus dados serão utilizados para:")
        print("• Cadastro de sócio torcedor")
        print("• Compra de ingressos")
        print("• Relatórios internos")
        print("• Segurança e autenticação\n")

        print("🔒 Todos os dados seguem as diretrizes da LGPD.\n")

        print("=" * 70)
        print("[1] ✅ Aceitar termos")
        print("[2] 📑 Ler política completa")
        print("[0] ❌ Cancelar cadastro")
        print("=" * 70)

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n\033[31m❌ Digite apenas números!\033[0m\n")
            continue

        match escolha:
            case 1:
                print("\n" + "-" * 50)
                print("✅ Você aceitou os termos de uso.".center(50))
                print("-" * 50 + "\n")
                return True
            case 2:
                return mostrar_politica()
            case 0:
                print("\nCadastro cancelado.")
                return False
            case _:
                print("\n\033[31m❌ Opção inválida!\033[0m\n")


def mostrar_politica():
    print("\n" + "=" * 70)
    print("\033[1;35m📑 POLÍTICA DE PRIVACIDADE\033[0m".center(70))
    print("=" * 70)

    print("Esta aplicação coleta e armazena dados pessoais")
    print("fornecidos durante o processo de cadastro.\n")

    print("\033[1;33m📌 Finalidade:\033[0m")
    print("• Cadastro de sócio torcedor")
    print("• Compra de ingressos")
    print("• Comunicação e autenticação\n")

    print("\033[1;33m🔒 Proteção:\033[0m")
    print("• Os dados são armazenados com segurança")
    print("• Nenhum dado será compartilhado sem consentimento\n")

    print("\033[1;33m⚖️ Direitos do usuário:\033[0m")
    print("• Solicitar acesso aos dados cadastrados")
    print("• Corrigir informações incorretas")
    print("• Solicitar exclusão dos dados\n")

    print("Ao aceitar, você concorda com o uso dos dados conforme descrito.\n")

    print("=" * 70)
    print("[1] ✅ Aceitar termos")
    print("[0] ❌ Cancelar cadastro")
    print("=" * 70)

    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n\033[31m❌ Digite apenas números!\033[0m\n")
            continue

        match escolha:
            case 1:
                print("\n" + "-" * 50)
                print("✅ Você aceitou os termos de uso.".center(50))
                print("-" * 50 + "\n")
                return True
            case 0:
                print("\nCadastro cancelado.")
                return False
            case _:
                print("\n\033[31m❌ Opção inválida!\033[0m\n")