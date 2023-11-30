# Função de leitura

def leitora_numeros():
    """ Essa função le dois numeros, só para quando definir os dois numeros, e transforma numa lista.)"""
    i=0
    numeros=[]
    while i<2:
        numeros.append(float(input(f"Digite o {i+1}º número que deseja operar")))
        i+=1
    return numeros

# Função que lê a operação que deve ser executada

def leitora_operacao():
    """ Le qual a operação desejada, dentro das 4 permitidas """

    operacao = input("Digite a operação que deseja realizar. ( + , - , * , / )")
    if operacao == '+':
        operador = 'soma'
    elif operacao == '-':
        operador = 'subtracao'
    elif operacao == '*':
        operador = 'multiplicacao'
    else:
        operador = 'divisao'
    
    return operador

def leitora():
    
    """ Junta a lista de numeros e a operacao em uma lista só """
    
    lista_numeros = leitora_numeros()
    operacao = leitora_operacao()
    
    return [lista_numeros,operacao]

def escritora(resultado: float) -> None:
    """Esta função coloca o resultado na tela. Retorno é none pq é um procedimento."""
    print(f" O resultado da operacao é igual a {resultado}")