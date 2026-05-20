import pwinput

SENHA_ADM = "unip2026"

def autenticar_adm():

    tentativas = 3

    while tentativas > 0:

        print("\n" + "-" * 40)
        print("🔒 ÁREA RESTRITA - ADMINISTRADOR".center(40))
        print("-" * 40 + "\n")

        senha = pwinput.pwinput("Digite a senha de administrador: ")

        if senha == SENHA_ADM:

            print("\n✅ Acesso autorizado!\n")
            return True

        tentativas -= 1

        print(f"\n❌ Senha incorreta! Tentativas restantes: {tentativas}")

    print("\n🚫 Número máximo de tentativas atingido!\n")

    return False