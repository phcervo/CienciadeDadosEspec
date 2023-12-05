# Função logaritmica
import numpy as np
import matplotlib.pyplot as plt


def logaritmo(y):
    return x ** (1/y)

x = np.linspace(1,16,100)
y= logaritmo(2)

# Processamento

plt.plot(x,y,'r')
plt.title('Função Logaritmo')
plt.xlabel('Eixo x',fontsize=12,color='green')
plt.ylabel('Eixo y',fontsize=14,color='blue')

# Saída de dados

plt.show()