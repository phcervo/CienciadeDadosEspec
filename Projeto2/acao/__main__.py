import es

# importando o modulo direto
from proc import Acao

def main():
    
    # leitura de dados
    dados = es.leitora()
    
    #instanciamento do objeto
    acao= Acao(dados[0],dados[1])
    
    # saida de daods
    es.impressora(acao)
    
if __name__ == "__main__":
    main()