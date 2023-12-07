# Módulo de busca de página- getter

# Importação dos módulos
import requests

# Função get_web
from typing import Any
def get_web(nome_pagina: str) -> Any:
    """ Está função busca páginas na web""" 
    pass

# Buscar dados no site
r = requests.get('https://api.github.com/events')
print(type(r))

# Enviar informações e gravar dados
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(type(r))

# Conteúdo da resposta
r = requests.get('https://api.github.com/events')
r.text

# Serve para descobrir a codificação 
r.encoding

r.encoding = 'ISO-8859-1'

# Conteúdo de resposta binária
r.content

# Criar uma imagem a partir de dados binários retornados por uma solicitação

from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content))

# Conteúdo de resposta JSON
## Possui também um decodificador JSON interno.
import requests
r = requests.get('https://api.github.com/events')
r.json()

# Conteúdo bruto da resposta
r = requests.get('https://api.github.com/events', stream=True)

r.raw

r.raw.read(10)

with open("arquivo", 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
        
# Abrindo arquivos com Python

arquivo2 = open("arquivo2.txt", 'w')
arquivo2.close()

casa = "A casa é bonita"

arquivo_casa = open("casa.txt", "w")

import io
arquivo_casa = io.StringIO(casa)

arquivo_casa.close()

with open("arquivo3.txt", 'w') as arquivo3:
    arquivo3.write("cansei.")