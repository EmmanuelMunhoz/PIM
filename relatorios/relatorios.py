from dados import (
    carregar_socios,
    carregar_ingressos,
    carregar_vendas
)

from modulos.utils import menu_atualizar_voltar

FRASE_OPCAO_INVALIDA = "\n❌ Opção inválida!\n"

# =========================
# MENU RELATÓRIOS
# =========================

def relatorio_socios():

    while True:

        socios = carregar_socios()

        total_socios = len(socios)

        ativos = 0
        inativos = 0

        ouro = 0
        prata = 0
        bronze = 0
        social = 0

        for socio in socios:

            if socio["status"] == "Ativo":
                ativos += 1

            else:
                inativos += 1

            if socio["plano"] == "Ouro":
                ouro += 1

            elif socio["plano"] == "Prata":
                prata += 1

            elif socio["plano"] == "Bronze":
                bronze += 1

            elif socio["plano"] == "Social":
                social += 1

        print("\n" + "=" * 40)
        print("RELATÓRIO DE SÓCIOS".center(40))
        print("=" * 40 + "\n")

        print(f"👥 Total de sócios: {total_socios}")
        print(f"✅ Sócios ativos: {ativos}")
        print(f"❌ Sócios inativos: {inativos}")

        print("\n🏆 POR PLANOS\n")

        print(f"🥇 Ouro: {ouro}")
        print(f"🥈 Prata: {prata}")
        print(f"🥉 Bronze: {bronze}")
        print(f"🤝 Social: {social}")

        escolha = menu_atualizar_voltar()

        match escolha:

            case 1:
                continue

            case 0:
                break

            case _:
                print("FRASE_OPCAO_INVALIDA")


# =========================
# LISTAR SÓCIOS
# =========================

def listar_socios():

    while True:

        socios = carregar_socios()

        print("\n" + "=" * 40)
        print("LISTA DE SÓCIOS".center(40))
        print("=" * 40 + "\n")

        if not socios:

            print("🚫 Nenhum sócio cadastrado.\n")

        else:

            for numero, socio in enumerate(socios, start=1):

                print(f"👤 SÓCIO #{numero}")
                print("-" * 40)

                print(f"🆔 ID: {socio['id_socio']}")
                print(f"📛 Nome: {socio['nome']}")
                print(f"🎂 Idade: {socio['idade']}")
                print(f"⚧️  Gênero: {socio['genero']}")
                print(f"📧 Email: {socio['email']}")
                print(f"📱 Telefone: {socio['telefone']}")
                print(f"🏆 Plano: {socio['plano']}")
                print(f"📌 Status: {socio['status']}")

                print("-" * 40)

        escolha = menu_atualizar_voltar()

        match escolha:

            case 1:
                continue

            case 0:
                break

            case _:
                print("FRASE_OPCAO_INVALIDA")


# =========================
# RELATÓRIO INGRESSOS
# =========================

def relatorio_ingressos():

    while True:

        ingressos = carregar_ingressos()

        vendas = carregar_vendas()

        disponiveis = ingressos["disponiveis"]

        vendidos = 0

        for venda in vendas:
            vendidos += venda["quantidade"]

        print("\n" + "=" * 40)
        print("RELATÓRIO DE INGRESSOS".center(40))
        print("=" * 40 + "\n")

        print(f"🎟️  Ingressos disponíveis: {disponiveis}")
        print(f"🧾 Ingressos vendidos: {vendidos}")

        escolha = menu_atualizar_voltar()

        match escolha:

            case 1:
                continue

            case 0:
                break

            case _:
                print("FRASE_OPCAO_INVALIDA")


# =========================
# RELATÓRIO FINANCEIRO
# =========================

def relatorio_financeiro():

    while True:

        socios = carregar_socios()

        vendas = carregar_vendas()

        total_planos = 0

        for socio in socios:

            if socio["plano"] == "Ouro":
                total_planos += 450

            elif socio["plano"] == "Prata":
                total_planos += 250

            elif socio["plano"] == "Bronze":
                total_planos += 89.90

        total_ingressos = 0

        quantidade_ingressos = 0

        for venda in vendas:

            total_ingressos += venda["valor_total"]

            quantidade_ingressos += venda["quantidade"]

        total_geral = total_planos + total_ingressos

        if quantidade_ingressos > 0:

            ticket_medio = (
                total_ingressos / quantidade_ingressos
            )

        else:
            ticket_medio = 0

        print("\n" + "=" * 40)
        print("RELATÓRIO FINANCEIRO".center(40))
        print("=" * 40 + "\n")

        print(
            f"🏆 Arrecadação Com: Planos: "
            f"R${total_planos:,.2f}".replace(",", ".")
        )

        print(
            f"🎟️  Arrecadação Com: Ingressos: "
            f"R${total_ingressos:,.2f}".replace(",", ".")
        )

        print(
            f"\n💰 Arrecadação Total: "
            f"R${total_geral:,.2f}".replace(",", ".")
        )

        print(
            f"🧾 Ticket médio: "
            f"R${ticket_medio:,.2f}".replace(",", ".")
        )

        escolha = menu_atualizar_voltar()

        match escolha:

            case 1:
                continue

            case 0:
                break

            case _:
                print("FRASE_OPCAO_INVALIDA")