
import numpy as np

# Função (x,y) quadratica

def quadratica(a,b):
    x = np.linspace(-4,4,100)
    y = a *(x*x) + b
    return [x,y]

def afim(a,b):
    x = np.linspace(-4,4,100)
    y = a*x+b
    return [x,y]

# Função exponencial

def exponencial():
    x = np.linspace(1,15,100)
    y = x ** 2
    return [x,y]

# Função logaritmica

def logaritmo():
    x = np.linspace(1,16,100)
    y = x ** (1/2)
    return [x,y]
