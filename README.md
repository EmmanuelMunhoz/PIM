# PIM - Sócio Torcedor do Peixão

Sistema em Python para cadastro de sócio torcedor, compra de ingressos e geração de relatórios.

# Descrição

Este projeto implementa um sistema de terminal para:

* Cadastro de sócios torcedores
* Busca e edição de cadastro
* Compra de ingressos
* Geração de relatórios administrativos
* Autenticação de administrador

# Requisitos

* Python 3.10 ou superior
* Pip instalado
* Biblioteca `pwinput`

# Estrutura do Projeto

* `main.py` — ponto de entrada do sistema
* `dados.py` — leitura e gravação de dados JSON
* `termos.py` — termos LGPD
* `autenticacao/` — autenticação de administrador
* `modulos/` — cadastro, planos, ingressos e validações
* `relatorios/` — relatórios e menus administrativos
* `dados/` — arquivos JSON do sistema

# Instalação Rápida

```powershell
pip install -r requirements.txt
python main.py
```
## Executar o sistema

```powershell
python main.py
```
# Dependências

* `pwinput`

# Observações

* O sistema cria automaticamente os arquivos JSON necessários.
* Execute sempre o projeto pela raiz da pasta.
* O projeto utiliza `match/case`, portanto exige Python 3.10+.

# Possíveis Problemas

* Caso o `pwinput` não esteja instalado, ocorrerá erro de importação.
* A pasta `dados/` deve permanecer com esse nome em minúsculo.