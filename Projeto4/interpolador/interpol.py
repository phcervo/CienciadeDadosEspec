import numpy as np
import scipy as sci
from collections.abc import Callable


def ajusta_curva(pontos:list)->Callable:
    # Função interp1d do metodo interpolate, tem que definir alguns parâmetros
    x=np.array(pontos[0])
    y=np.array(pontos[1])
    f=sci.interpolate.interp1d(x,y)
    return f