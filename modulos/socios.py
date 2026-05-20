import pwinput

from dados import (
    carregar_socios,
    salvar_socios,
    buscar_socio_por_id
)

from modulos.utils import (
    gerar_id,
    pedir_idade,
    validar_genero,
    status_plano,
    pedir_senha,
    validar_nome,
    validar_telefone,
    validar_email,
    validar_senha
)

from termos import termo_lgpd

from modulos.planos import escolha_seu_plano

from modulos.ingressos import mostrar_historico_vendas


# =========================
# CADASTRO
# =========================

def cadastro_socio_torcedor():

    if not termo_lgpd():
        return

    idade = pedir_idade()

    if idade is None:
        return

    nome = validar_nome()

    genero = validar_genero()

    telefone = validar_telefone()

    email = validar_email()

    plano = escolha_seu_plano()

    status = status_plano()

    senha = pedir_senha()

    dados = carregar_socios()

    id_socio = gerar_id(dados)

    novo_socio = {
        "id_socio": id_socio,
        "idade": idade,
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "genero": genero,
        "plano": plano,
        "status": status,
        "senha": senha
    }

    dados.append(novo_socio)

    salvar_socios(dados)

    print("\n✅ Cadastro realizado com sucesso!")
    print(f"🆔 Seu ID é: {id_socio}\n")


# =========================
# LOGIN
# =========================

def buscar_socio():

    while True:

        try:
            id_torcedor = int(
                input("Qual o seu ID de Sócio Torcedor? ")
            )

        except ValueError:
            print("\n❌ Digite um número válido!\n")
            continue

        socio = buscar_socio_por_id(id_torcedor)

        if socio is None:
            print("\n❌ Sócio torcedor não encontrado\n")
            continue

        print("\n✅ Sócio torcedor encontrado\n")

        if not validar_senha(socio):
            return

        menu_socio(socio)
        return


# =========================
# MENU DO SÓCIO
# =========================

def menu_socio(socio):

    while True:

        socio = buscar_socio_por_id(
            socio["id_socio"]
        )

        if socio is None:
            print("\n🚫 Usuário não existe mais.\n")
            return

        print("\n==============================")
        print(f"👋 Bem-vindo, {socio['nome']}")
        print("==============================")
        print("[1] Ver meus dados")
        print("[2] Editar cadastro")
        print("[3] Excluir cadastro")
        print("[4] Histórico de compras")
        print("[0] Sair")

        try:
            opcao = int(input("\nEscolha uma opção: "))

        except ValueError:
            print("\n❌ Digite uma opção válida!\n")
            continue

        match opcao:

            case 1:
                mostrar_dados_socio(socio)

            case 2:
                editar_socio(socio)

            case 3:
                excluir_conta(socio)
                return

            case 4:
                mostrar_historico_vendas(socio)

            case 0:
                print("\n👋 Saindo do painel...\n")
                return

            case _:
                print("\n❌ Opção inválida\n")


# =========================
# MOSTRAR DADOS
# =========================

def mostrar_dados_socio(socio):

    print("\n📄 DADOS DO SÓCIO\n")

    for chave, valor in socio.items():

        chave_formatada = chave.capitalize()

        print(f"{chave_formatada}: {valor}")


# =========================
# EDITAR CADASTRO
# =========================

def editar_socio(socio):

    dados = carregar_socios()

    for item in dados:

        if item["id_socio"] != socio["id_socio"]:
            continue

        while True:

            print("\n========================")
            print("✏️ EDITAR CADASTRO")
            print("========================")
            print("[1] Nome")
            print("[2] Telefone")
            print("[3] Email")
            print("[4] Plano")
            print("[5] Status")
            print("[0] Sair")

            try:
                opcao = int(input("\nEscolha: "))

            except ValueError:
                print("\n❌ Digite uma opção válida!\n")
                continue

            match opcao:

                case 1:
                    editar_nome(item, dados)

                case 2:
                    editar_telefone(item, dados)

                case 3:
                    editar_email(item, dados)

                case 4:
                    editar_plano(item, dados)

                case 5:
                    editar_status(item, dados)

                case 0:
                    print("\n👋 Saindo da edição...\n")
                    return

                case _:
                    print("\n❌ Opção inválida\n")


# =========================
# FUNÇÕES DE EDIÇÃO
# =========================

def editar_nome(socio, dados):

    socio["nome"] = validar_nome()

    salvar_socios(dados)

    print("\n✅ Nome atualizado!\n")


def editar_telefone(socio, dados):

    socio["telefone"] = validar_telefone()

    salvar_socios(dados)

    print("\n✅ Telefone atualizado!\n")


def editar_email(socio, dados):

    socio["email"] = validar_email()

    salvar_socios(dados)

    print("\n✅ Email atualizado!\n")


def editar_plano(socio, dados):

    plano_atual = socio["plano"]

    novo_plano = escolha_seu_plano()

    if plano_atual == novo_plano:
        print("\n⚠️ Você já está nesse plano\n")
        return

    socio["plano"] = novo_plano

    salvar_socios(dados)

    print("\n✅ Plano atualizado!\n")


def editar_status(socio, dados):

    socio["status"] = status_plano()

    salvar_socios(dados)

    print("\n✅ Status atualizado!\n")


# =========================
# EXCLUIR CONTA
# =========================

def excluir_conta(socio):

    print("\n====================================")
    print("⚠️ EXCLUSÃO DE CONTA")
    print("====================================")

    senha = pwinput.pwinput(
        "\nDigite sua senha para confirmar: "
    )

    if senha != socio["senha"]:
        print("\n❌ Senha incorreta.\n")
        return

    confirmar = input(
        "\nDigite SIM para confirmar: "
    ).upper().strip()

    if confirmar != "SIM":
        print("\n❌ Exclusão cancelada.\n")
        return

    dados = carregar_socios()

    dados_filtrados = []

    for item in dados:

        if item["id_socio"] != socio["id_socio"]:
            dados_filtrados.append(item)

    salvar_socios(dados_filtrados)

    print("\n✅ Conta excluída com sucesso!\n")