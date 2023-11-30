"""
Modulo Proc
Descrição: Esse módulo provÊ funções da calculadora básica.
Autor: Pedro Henrique Cervo
Versão: 0.0.1
Data: 29/11/2023

"""

def somadora(numero1:float,numero2:float) -> float:
    """ Esta função pega dois numeros reais e retorna a soma deles"""
    return numero1 + numero2

def diminuidora(numero1:float,numero2:float) -> float:
    """ Esta função pega dois numeros reais e retorna a subtração deles"""
    return numero1 - numero2

def mult(numero1:float,numero2:float) -> float:
    """ Esta função pega dois numeros reais e retorna o produto deles"""
    return numero1 * numero2

def div(numero1:float,numero2:float) -> float:
    """ Esta função pega dois numeros reais e retorna a divisão deles"""
    while numero2==0:
        print("Divisão por 0 é inválida")
        numero2=input("escolha outro número: ")
        
    return numero1 / numero2
   