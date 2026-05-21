from datetime import datetime
import random
import string
from dados import buscar_socio_por_id,carregar_ingressos,salvar_ingressos,carregar_vendas,salvar_vendas
from modulos.utils import validar_senha

MENSAGEM_VALOR_INVALIDO = "❌ Digite um valor válido\n"
MENSAGEM_PAGAMENTO_CANCELADO = "\n❌ Pagamento cancelado\n"


def comprar_ingressos():
    socio = autenticar_socio()

    if socio is None:
        return
    
    if socio["status"] != "Ativo":
        print(f"\nSua mensalidade está [{socio['status']}] ❌")
        print("Regularize para comprar o ingresso.\n")
        return
    
    print(f"\n🎟️  Bem Vindo [\033[92m{socio['nome']}\033[0m]")     
    
    menu_ingresso(socio)

def autenticar_socio():

    while True:

        try:
            id_torcedor = int(input("\nDigite seu ID Sócio Torcedor: "))

            socio = buscar_socio_por_id(id_torcedor)

            if socio is None:
                print("\nSócio torcedor não encontrado ❌")
                continue
            print("\nSócio torcedor encontrado ✅\n")

            if not validar_senha(socio):
                return None
            return socio

        except ValueError:
            print("ID Inválido, digite novamente!\n")

def menu_ingresso(socio):
    
    while True:
        quantidade_ingressos = carregar_ingressos()

        
        print(f"\n🎟️  Ingressos Disponiveis: \033[92m{quantidade_ingressos['disponiveis']}\033[0m\n")
        print("=" * 40)
        print("São Paulo vs Santos\n".center(40))
        print("Jogo: 29/07/2026 - 21:30 - Morumbi-SP")
        print("=" * 40)
        print("Guichê Online".center(40))
        print("=" * 40)
        print("\n[1] Comprar Ingresso")
        print("[0] Sair\n")

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite uma opção Válida!")
            continue

        match escolha:
            case 1:
                comprar(socio)
                break
            case 0:
                break
            case _:
                print("Escolha entre as opções 1 ou 0")

def comprar(socio):

    while True:
        quantidade_ingressos = carregar_ingressos()
        try:
            
            if quantidade_ingressos['disponiveis'] <= 0:
                print("\n❌ Ingressos esgotados!\n")
                break

            ingresso = 125.00
            print(f"\nValor do ingresso: R${ingresso:.2f}")
            quantidade = int(input("\nQuantos ingressos você quer comprar? "))

            if quantidade <= 0:
                print("❌ Quantidade inválida")
                continue

            if quantidade > quantidade_ingressos['disponiveis']:
                print("❌ Quantidade de ingressos Indisponiveis")
                continue

            print(f"\nConfirmar compra de {quantidade} ingressos?\n")
            print("[1] Sim")
            print("[2] Alterar")
            print("[0] Sair\n")

            while True:
                try:
                    confirmar = int(input("Escolha: "))
                except ValueError:
                    print("\n❌ Opção Inválida\n")
                    continue

                match confirmar:
                    case 1:
                        finalizar_compra(socio,quantidade,ingresso)
                        return
                    case 2:
                        break
                    case 0:
                        break
        except ValueError:
            print(MENSAGEM_VALOR_INVALIDO)

def finalizar_compra(socio, quantidade, ingresso):

    valor_total = quantidade * ingresso
    plano = socio['plano']

    valor_final, economia, desconto = calcular_desconto(plano, valor_total)

    print("\n========================================")
    print("RESUMO DA COMPRA".center(40))
    print("========================================")

    print(f"\n🎟️  Quantidade: {quantidade}")
    print(f"💰 Valor total: R${valor_total:.2f}")
    print(f"🏷️  Plano: {plano}")
    print(f"📉 Desconto: {desconto * 100:.0f}%")
    print(f"💵 Economia: R${economia:.2f}")
    print(f"✅ Valor final: R${valor_final:.2f}")

    if plano == "Ouro":

        print("\n✅ Compra finalizada com sucesso!")

        quantidade_ingressos = carregar_ingressos()
        quantidade_ingressos['disponiveis'] -= quantidade
        salvar_ingressos(quantidade_ingressos)

        registrar_venda(socio, quantidade, 0, "Grátis")
        return

    forma_pagamento = menu_pagamento()

    if forma_pagamento is None:
        return

    quantidade_ingressos = carregar_ingressos()

    quantidade_ingressos['disponiveis'] -= quantidade

    salvar_ingressos(quantidade_ingressos)

    registrar_venda(socio,quantidade,valor_final,forma_pagamento)

    print("\n✅ Compra finalizada com sucesso!")


def calcular_desconto(plano,valor_total):

    match plano:
        case "Ouro":
            desconto = 1.0

        case "Social":
            desconto = 0.8

        case "Prata":
            desconto = 0.5

        case "Bronze":
            desconto = 0.2

    valor_final = round(valor_total * (1 - desconto), 2)
    economia = round(valor_total - valor_final, 2)

    return valor_final,economia,desconto

def menu_pagamento():

    while True:
        print("=" *40)
        print("Formas de Pagamento\n".center(40))
        print("[1] - Pix")
        print("[2] - Cartão - Debitão/Crédito")
        print("[3] - Boleto bancário")
        print("[0] - Voltar")

        try:
            escolha = int(input("Escolhar uma opção: "))
        except ValueError:
            print(MENSAGEM_VALOR_INVALIDO)
            continue

        match escolha:
            case 1:
                forma_pagamento = gerar_codigo_pix()
                return forma_pagamento
            case 2:
                forma_pagamento = pagamento_cartao()
                return forma_pagamento
            case 3:
                forma_pagamento = gerar_boleto()
                return forma_pagamento
            case 0:
                print(MENSAGEM_PAGAMENTO_CANCELADO)
                return None
            case _ :
                print("Digite um valor entre [0,1,2 ou 3]")

def registrar_venda(socio, quantidade, valor_final, forma_pagamento):
    
    vendas = carregar_vendas()

    novo_id_venda = len(vendas) + 1

    nova_venda = {
        "id_venda": novo_id_venda,
        "id_socio": socio["id_socio"],
        "nome": socio["nome"],
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "quantidade": quantidade,
        "valor_total": round(valor_final, 2),
        "pagamento": forma_pagamento,
        "plano": socio["plano"]
    }

    vendas.append(nova_venda)

    salvar_vendas(vendas)

def gerar_codigo_pix():

    caracteres = string.ascii_lowercase + string.digits

    identificador = ''.join(random.choice(caracteres) for _ in range(32))

    chave_pix = f"00020126580014BR.GOV.BCB.PIX0136{identificador}"

    print("\n🔑 Chave PIX gerada com sucesso!\n")
    print(f"\n{chave_pix}\n")

    while True:

        print("\n[1] Confirmar pagamento")
        print("[0] Cancelar")

        try:
            confirmar = int(input("\nEscolha: "))
        except ValueError:
            print(MENSAGEM_VALOR_INVALIDO)
            continue

        match confirmar:

            case 1:
                print("\n✅ Pagamento via PIX confirmado!\n")
                return "Pix"

            case 0:
                print(MENSAGEM_PAGAMENTO_CANCELADO)
                return None

            case _:
                print("Escolha uma opção válida")

def pagamento_cartao():

    while True:

        numero = input("\nDigite os 16 números do cartão: ").strip()

        if not numero.isdigit() or len(numero) != 16:
            print("❌ Cartão inválido")
            continue

        validade = input("Digite a validade (MM/AA): ").strip()

        if not validar_validade_cartao(validade):
            print("❌ Validade inválida ou cartão vencido")
            continue

        cvv = input("Digite o CVV: ").strip()

        if not cvv.isdigit() or len(cvv) != 3:
            print("❌ CVV inválido")
            continue

        print("\n💳 Processando pagamento...\n")
        print("✅ Pagamento aprovado!\n")

        return "Cartão"

def validar_validade_cartao(validade):
    try:
        mes, ano = validade.split("/")

        if len(mes) != 2 or len(ano) != 2:
            return False

        if not (mes.isdigit() and ano.isdigit()):
            return False

        mes = int(mes)
        ano = 2000 + int(ano)

        if mes < 1 or mes > 12:
            return False

        hoje = datetime.now()

        if ano < hoje.year or (ano == hoje.year and mes < hoje.month):
            return False

        return True
    except ValueError:
        return False

def gerar_boleto():

    grupos = []

    for _ in range(5):
        numero = ''.join(str(random.randint(0,9)) for _ in range(11))
        grupos.append(numero)

    codigo_boleto = ' '.join(grupos)

    print("\n📄 Boleto gerado com sucesso!\n")
    print(codigo_boleto)

    while True:

        print("\n[1] Confirmar pagamento")
        print("[0] Cancelar")

        try:
            confirmar = int(input("Escolha: "))
        except ValueError:
            print(MENSAGEM_VALOR_INVALIDO)
            continue

        match confirmar:

            case 1:
                print("\n✅ Pagamento via boleto confirmado!\n")
                return "Boleto"

            case 0:
                print(MENSAGEM_PAGAMENTO_CANCELADO)
                return None

            case _:
                print("Escolha uma opção válida")

def mostrar_historico_vendas(socio):

    historico_vendas = []

    vendas = carregar_vendas()

    for venda in vendas:

        if venda["id_socio"] == socio["id_socio"]:

            historico_vendas.append(venda)

    if not historico_vendas:
        print("\n🚫 Nenhuma compra encontrada.\n")
        input("Pressione ENTER para voltar...")
        return

    total_gasto = 0
    total_ingressos = 0

    for venda in historico_vendas:

        total_gasto += venda["valor_total"]
        total_ingressos += venda["quantidade"]

    print("\n" + "=" * 40)
    print("📜 HISTÓRICO DE COMPRAS".center(40))
    print("=" * 40)

    print(f"\n👤 Sócio: {socio['nome']}")
    print(f"🎟️  Total de ingressos comprados: {total_ingressos}")
    print(f"💰 Total gasto: R$ {total_gasto:.2f}")

    print("\n" + "=" * 40)
    print("🎫 COMPRAS".center(40))
    print("=" * 40)

    for numero, venda in enumerate(historico_vendas, start=1):

        print(f"🧾 Venda #{numero}")
        print(f"📅 Data: {venda['data']}")
        print(f"🎟️  Quantidade: {venda['quantidade']}")
        print(f"💰 Valor: R$ {venda['valor_total']:.2f}")
        print(f"💳 Pagamento: {venda['pagamento']}")
        print(f"🏆 Plano: {venda['plano']}")

        print("-" * 30)

    input("\nPressione ENTER para voltar...")


    