from modulos.socios import (cadastro_socio_torcedor,buscar_socio)

from modulos.ingressos import comprar_ingressos

from autenticacao.autenticacao_adm import autenticar_adm

from relatorios.menu_relatorios import menu_relatorios

def menu():

    while True:

        print("\n" + "=" * 41)
        print("BEM VINDO AO SOCIO TORCEDOR DO PEIXÃO".center(40))
        print("=" * 41)
        print("MENU DE ESCOLHAS".center(40))
        print("=" * 41 + "\n")

        print(" [1] - 📝 Cadastro Sócio Torcedor")
        print(" [2] - 🔍 Buscar Sócio Torcedor")
        print(" [3] - 🎟️  Comprar Ingresso")
        print(" [4] - 📊 Relatório (ADM)")
        print(" [0] - ❌ Sair\n")

        try:
            escolha = int(input("Escolha uma opção: "))

        except ValueError:
            print("\n\033[31m❌ Digite apenas números!\033[0m\n")
            continue

        match escolha:

            case 1:
                cadastro_socio_torcedor() #Está dentro de modulos/socios.py

            case 2:
                buscar_socio()

            case 3:
                comprar_ingressos()

            case 4:
                if autenticar_adm():
                    menu_relatorios()

            case 0:
                print("\nSaindo do sistema...\n")
                break

            case _:
                print("\n\033[31m❌ Opção inválida!\033[0m\n")

menu() # teste