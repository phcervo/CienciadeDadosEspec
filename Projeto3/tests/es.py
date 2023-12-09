# Criação da função de escolha:
import numpy as np
import matplotlib.pyplot as plt

def leitor_funcao():
    funcao = int(input ("Escolha a função que deseja plotar o gráfico : (1-Afim , 2-Quadrática, 3-Exponencial, 4 - Logaritmica) "))
    return funcao

def leitor_coeficientes():
    """ Essa função retorna os coeficientes a e c definidas para a função."""
    
    coef_a = float(input("Defina o coeficiente a: "))
    coef_b = float(input("Defina o coeficiente b: "))

    return [coef_a, coef_b]



def impressora(valores: list, funcao) -> None:
    plt.plot(valores[0],valores[1])
    plt.title(funcao)
    plt.xlabel('Eixo x',fontsize=12,color='blue')
    plt.ylabel('Eixo y',fontsize=12,color='blue')

    plt.show()