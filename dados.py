import json
from pathlib import Path

# =========================
# PASTA DE DADOS
# =========================

PASTA_DADOS = Path("dados")

PASTA_DADOS.mkdir(exist_ok=True)

ARQUIVO_SOCIOS = PASTA_DADOS / "socios.json"
ARQUIVO_INGRESSOS = PASTA_DADOS / "ingressos.json"
ARQUIVO_VENDAS = PASTA_DADOS / "vendas.json"

# =========================
# SÓCIOS
# =========================

def garantir_socios():

    if not ARQUIVO_SOCIOS.exists():
        ARQUIVO_SOCIOS.write_text("[]", encoding="utf-8")


def carregar_socios():

    garantir_socios()

    with open(ARQUIVO_SOCIOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_socios(dados):

    garantir_socios()

    with open(ARQUIVO_SOCIOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def buscar_socio_por_id(id_torcedor):

    dados = carregar_socios()

    for socio in dados:

        if socio["id_socio"] == id_torcedor:
            return socio

    return None


# =========================
# INGRESSOS
# =========================

def garantir_ingressos():

    if not ARQUIVO_INGRESSOS.exists():

        dados_iniciais = {
            "disponiveis": 100
        }

        ARQUIVO_INGRESSOS.write_text(
            json.dumps(dados_iniciais, indent=4, ensure_ascii=False),
            encoding="utf-8"
        )


def carregar_ingressos():

    garantir_ingressos()

    with open(ARQUIVO_INGRESSOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_ingressos(dados):

    garantir_ingressos()

    with open(ARQUIVO_INGRESSOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


# =========================
# VENDAS
# =========================

def garantir_vendas():

    if not ARQUIVO_VENDAS.exists():
        ARQUIVO_VENDAS.write_text("[]", encoding="utf-8")


def carregar_vendas():

    garantir_vendas()

    with open(ARQUIVO_VENDAS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_vendas(dados):

    garantir_vendas()

    with open(ARQUIVO_VENDAS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)