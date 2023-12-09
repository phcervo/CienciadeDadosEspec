import numpy as np
import matplotlib.pyplot as plt
from collections.abc import Callable

def leitor_pontos() -> list:
    """ Retorna uma lista de ndarrays"""
    n=1
    lista_x=[]
    lista_y=[]
    resposta=1
    print("Digite as coordenadas X em ordem crescente.")
    
    while resposta!='0':
        cordx=float(input(f"Digite o valor da coordenada x do {n}ª ponto: "))
        cordy=float(input(f"Digite o valor da coordenada y do {n}ª ponto: "))
        
        lista_x.append(cordx)
        lista_y.append(cordy)
        
        resposta=input("Deseja adicionar um novo ponto? (Digite 0 para Não)")
        
        n+=1
        lista_x.sort()
        #lista_y.sort()
        
    return [lista_x,lista_y]
    
    
def plota_grafico(pontos: list, f: Callable) -> None:
    """ Esta função plota o gráfico dada uma lista de pontos"""
    x=pontos[0]
    y=f(x)
    
    plt.plot(x,y,'-',x,y,'o')
    plt.show()