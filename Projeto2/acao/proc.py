
# Evoluindo a classe
class Acao:
    def __init__(self,emissor,codigo_b3):
        # self é a boa pratica para definir a noção do objeto (caracteristicas).
        self.emissor=emissor
        # O atributo emissor do objeto ação receberá a variavel emissor
        self.codigo_b3=codigo_b3
    
    # Criar o método str, para definir o modelo do print do objeto.
    def __str__(self):
        return f"O emissor da ação é {self.emissor} e o código é {self.codigo_b3}"
    
    def negociar(self):
        print("Metodo negociar() não implementado")
        # Define que o metodo nao esta implementado
        NotImplemented
        