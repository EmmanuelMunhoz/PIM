import random
import pwinput
from dados import carregar_socios

def pedir_idade():

    while True:

        try:
            idade = int(input("Sua idade? "))

        except ValueError:
            print("\n❌ Digite uma idade válida!\n")
            continue

        if idade < 18:
            print("\n❌ Cadastro permitido apenas para maiores de 18 anos.")
            print("Voltando ao menu...\n")
            return None

        if idade > 150:
            print("\n🧛 Idade inválida. Digite uma idade real.\n")
            continue

        return idade

def validar_nome():

    while True:

        nome = input("Seu nome: ").strip()
        nome_sem_espaco = nome.replace(" ", "")

        if len(nome_sem_espaco) < 3:
            print("\n❌ Nome muito curto!\n")
            continue

        if not nome:
            print("\n❌ Nome não pode ser vazio!\n")
            continue        

        if not nome_sem_espaco.isalpha():
            print("\n❌ O nome deve conter apenas letras!\n")
            continue

        return nome.title()


def validar_genero():

    opcoes_genero = {"H": "Homem","M": "Mulher","O": "Outro"}

    while True:

        genero = input("Seu gênero? [H] Homem | [M] Mulher | [O] Outro: ").upper().strip()

        if genero not in opcoes_genero:
            print("\n❌ Opção inválida!\n")
            continue

        return opcoes_genero[genero]

def validar_telefone():

    while True:

        telefone = input("Digite seu telefone (DDD + número): ").strip()

        if not telefone:
            print("\n❌ Telefone não pode ser vazio!\n")
            continue

        telefone_limpo = (
            telefone
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )

        if not telefone_limpo.isdigit():
            print("\n❌ O telefone deve conter apenas números!\n")
            continue

        if len(telefone_limpo) != 11:
            print("\n❌ O telefone deve conter 11 dígitos!\n")
            continue

        return telefone_limpo


def validar_email():

    while True:

        email = input("Digite seu email: ").strip().lower()

        if not email:
            print("\n❌ Email não pode ser vazio!\n")
            continue

        if " " in email:
            print("\n❌ Email não pode conter espaços!\n")
            continue

        if "@" not in email or "." not in email:
            print("\n❌ Email inválido! Deve conter '@' e '.'\n")
            continue

        if email.startswith("@"):
            print("\n❌ Email não pode começar com '@'!\n")
            continue

        if email.endswith("."):
            print("\n❌ Email não pode terminar com '.'!\n")
            continue

        return email
                
def status_plano():

    opcoes_status = {
        "A": "Ativo",
        "I": "Inativo/Inadimplente"
    }

    while True:

        status = input("Status do plano? [A] Ativo | [I] Inativo/Inadimplente: ").upper().strip()

        if status not in opcoes_status:
            print("\n❌ Opção inválida!\n")
            continue

        return opcoes_status[status]

def pedir_senha():

    while True:

        senha = pwinput.pwinput("Digite sua senha: ", mask="*").strip()

        if not senha:
            print("\n❌ A senha não pode ser vazia!\n")
            continue

        if len(senha) < 3:
            print("\n❌ A senha deve ter pelo menos 3 caracteres!\n")
            continue

        return senha

def gerar_id(dados):

    ids_existentes = {
        socio["id_socio"]
        for socio in dados
    }

    while True:

        novo_id = random.randint(100000, 999999)

        if novo_id not in ids_existentes:
            return novo_id

def validar_senha(socio):
    
    senha_correta = socio["senha"]
    tentativas = 3

    while tentativas > 0:

        senha = pwinput.pwinput(prompt="Digite sua senha: ", mask="*")

        if senha == senha_correta:
            return True

        tentativas -= 1
        print(f"\n❌ Senha incorreta. Tentativas restantes: {tentativas}\n")

    print("🚫 Acesso bloqueado. Muitas tentativas incorretas.\n")
    return False

def menu_atualizar_voltar():

    MENSAGEM_OPCAO_INVALIDA = "\n❌ Opção inválida\n"

    print("\n[1] Atualizar")
    print("[0] Voltar")

    try:
        escolha = int(input("\nEscolha: "))

    except ValueError:
        print(MENSAGEM_OPCAO_INVALIDA)
        return None

    return escolha