import es
import proc


# Definição de funções
def escolhedora(dados):
    if dados[1] == 'soma':
        resultado = proc.somadora(dados[0][0],dados[0][1])
    elif dados[1] == 'subtracao':
        resultado = proc.diminuidora(dados[0][0],dados[0][1])
    elif dados[1] == 'multiplicacao':
        resultado = proc.mult(dados[0][0],dados[0][1])
    else:
        resultado = proc.div(dados[0][0],dados[0][1])
        
    return resultado
 
def main():
    dados = es.leitora()
    resultado = escolhedora (dados)
    es.escritora(resultado)
    

# Execução

if __name__ == "__main__":
    main()
    