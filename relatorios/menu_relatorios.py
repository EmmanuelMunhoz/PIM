from relatorios.relatorios import (
    relatorio_socios,
    relatorio_ingressos,
    relatorio_financeiro,
    listar_socios
)

def menu_relatorios():

    while True:

        print("=" * 40)
        print("MENU PRINCIPAL - RELATÓRIOS".center(40))
        print("=" * 40 + "\n")

        print("[1] - Relatório de Sócios")
        print("[2] - Listar Sócios")
        print("[3] - Relatório de Ingressos")
        print("[4] - Relatório Financeiro")
        print("[0] - Voltar\n")

        try:
            escolha = int(input("Escolha uma opção: "))

        except ValueError:
            print("\n❌ Opção inválida!\n")
            continue

        match escolha:

            case 1:
                relatorio_socios()

            case 2:
                listar_socios()

            case 3:
                relatorio_ingressos()

            case 4:
                relatorio_financeiro()

            case 0:
                break

            case _:
                print("\n❌ Opção inválida!\n")