# Função get_web
from typing import Any
import requests


# Função que acessa a página pelo método requests e retorna o código fonte da pagina
def get_web(nome_pagina: str) -> Any:
    r = requests.get(nome_pagina)
    r.encoding = 'ISO-8859-1'

    codigo_fonte = r.text
    
    return codigo_fonte