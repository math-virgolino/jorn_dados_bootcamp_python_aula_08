import pandas as pd
import os
import glob


def extrair_dados(path: str) -> pd.DataFrame:
        arquivos_json = glob.glob(os.path.join(path, '*.json'))
        df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
        df_total = pd.concat(df_list, ignore_index=True)
        return df_total

def calcular_kpi_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    Parametros: "csv" e/ou "parquet" em uma lista
    """
    for i in format_saida:
        if i == "csv":
            df.to_csv("dados.csv")
        if i == "parquet":
            df.to_parquet("dados.parquet")

if __name__ == "__main__":
    pasta = "data"
    print(extrair_dados(path=pasta))