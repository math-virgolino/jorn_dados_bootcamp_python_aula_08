from etl import run_pipeline

pasta = 'data'
arquivos_saida = ["csv", "parquet"]
run_pipeline(pasta, arquivos_saida)