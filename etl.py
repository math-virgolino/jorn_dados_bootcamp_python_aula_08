import pandas as pd
import os
import glob


def extrair_dados(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


def calcular_kpi_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df


def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    Parametros: "csv" e/ou "parquet" em uma lista
    """
    for i in format_saida:
        if i == 'csv':
            df.to_csv('dados.csv', index=False)
        if i == 'parquet':
            df.to_parquet('dados.parquet', index=False)

def run_pipeline(path: str, arquivos_saida: list):
    dados = extrair_dados(path)
    dados = calcular_kpi_total_de_vendas(dados)
    carregar_dados(dados, arquivos_saida)
    
if __name__ == '__main__':
    pasta = 'data'
    arquivos_saida = ["csv", "parquet"]
    run_pipeline(pasta, arquivos_saida)