# Modulo de entrada e saída

# Importa a classe Acao que sera usada posteriormenet
from proc import Acao

#Função de leitura do emissor
def leitora_emissor():
    emissor = input("Qual o nome da empresa? ")
    return emissor

# Função de leitura do codigo B3
def leitora_codigo():
    codigo = input("Qual o código na B3? ")
    codigo = codigo.upper()
    return codigo

# Função leitora agregando as duas funções de leitura
def leitora():
    emissor = leitora_emissor()
    codigo = leitora_codigo()
    return emissor,codigo
 
# Metodo pra imprimir o resultado

def impressora (acao: Acao):
    """ imprime o resultado"""
    print(acao)

    