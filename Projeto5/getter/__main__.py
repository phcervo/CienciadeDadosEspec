import es
import getter

# Le a pagina web desejada pelo cliente:
nome_pagina = es.leitor_pagina()

# Retorna o código fonte da pagina
codigo_fonte = getter.get_web(nome_pagina)

# Imprime o arquivo com o codigo_fonte em formato .json

es.impressora(codigo_fonte)