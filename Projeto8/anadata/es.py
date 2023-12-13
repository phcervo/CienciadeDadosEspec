# Função para consumo da API
# Pandas trabalha bastante com dataframes

import numpy as np
import pandas as pd


# Função para input da URL

def get_url():
    url = input ("Digite a URL do arquivo .CSV que deseja analisar: ")
    
    return url

# Função que le o dataframe
def leitor_dados(url: str) -> pd.DataFrame:
    
    dados = pd.read_csv(url, sep =";" , encoding = "utf-8", decimal = ",")
    
    return dados


# Função para escolher a coluna de análise
def coluna_desejada()-> str:
    coluna = input("Qual coluna do DataFrame deseja analisar? ")
    
    return coluna

# Função para plotar o gráfico de análise
import matplotlib.pyplot as plt

def plotter(dados: pd.DataFrame, coluna: str) -> None:
    plt.plot(dados[coluna])
    plt.show()
    
# Função que printa as estatisticas
def imprime_estatistica(estatisticas: list) -> None:
    media = estatisticas[0]
    dp = estatisticas [1]
    
    print(f" A média da coluna desejada é {media}")
    print("\n")
    print(f" O desvio padrão dos dados da coluna desejada é {dp}")
    