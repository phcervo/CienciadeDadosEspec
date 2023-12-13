import numpy as np
import pandas as pd

# Função que mostra as colunas existentes no df

def colunas_existentes(dados: pd.DataFrame) -> None:
    colunas = dados.columns
    n_colunas = len(colunas)
    print(f"O número de colunas no dataframe é {n_colunas}")
    print("\n")
    print("Segue a lista das colunas existentes: ")
    print("\n")
    print(colunas)

# Função que calcula as estatisticas

def calcula_estatisticas(dados: pd.DataFrame,coluna: str) ->list:
    media = dados[coluna].mean()
    dp = dados[coluna].std()
    print("O resumo estatístico dos dados como um todo é o seguinte: ")
    print("\n")
    
    print(dados.describe())
    
    return [media,dp]