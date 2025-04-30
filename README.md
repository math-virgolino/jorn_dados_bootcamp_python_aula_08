# Projeto: ETL de Vendas
Este projeto realiza um processo de ETL (Extração, Transformação e Carga) de arquivos .json contendo dados de vendas, com cálculo de KPIs e exportação dos dados para os formatos CSV e Parquet.

## Estrutura do Projeto
```
.
├── data/                # Pasta com arquivos .json de entrada
├── etl.py               # Script principal de ETL
├── pyproject.toml       # Gerenciador de dependências com Poetry
├── poetry.lock          # Arquivo de lock das dependências
└── README.md            # Documentação do projeto
```
## Requisitos
* Python 3.12+
* Poetry (para gerenciamento de dependências)

## Funcionalidades
* Extração: Carrega todos os arquivos .json da pasta data/.
* Transformação: Calcula o KPI de Total de Vendas (Quantidade × Venda).
* Carga: Exporta os dados processados nos formatos CSV e/ou Parquet.

## Dependências Principais
* pandas: Manipulação de dados
* fastparquet: Suporte ao formato Parquet
* blue: Formatação e linting de código