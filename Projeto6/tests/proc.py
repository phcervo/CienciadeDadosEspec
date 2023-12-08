# funcao leitor_web

import requests
from bs4 import BeautifulSoup

def leitor_web(endereco_web: str) -> str:
    pagina = requests.get(endereco_web)
    return pagina.text


#Função acha tag

def extrator_tag(pagina: str, tag:str)->list:
    
    soup = BeautifulSoup(pagina,'html.parser')
    return soup.find(tag)
    

# Função que retorna titulo e contagem da palavra requirida

def extrator_total(pagina: str, tag:str)->list:
    
    soup = BeautifulSoup(pagina,'html.parser')
    titulo = soup.title.text
    body = soup.body.div.text
    contagem = body.count(tag)
    
    return titulo,contagem