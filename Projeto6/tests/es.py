# Escolher site, site padrão é "http://pythonscraping.com/pages/page1.html"

# Modulo leitor_site

def leitor_site()->str:
    escolha = int(input("Deseja escolher o site ? (1 - Sim , 2 - Não). Se não digitar, será escolhido o site http://pythonscraping.com/pages/page1.html"))
    if escolha != 2:
        endereco_web = input("Digite a URL do site: ")
    else:
        endereco_web = "http://pythonscraping.com/pages/page1.html"
    
    return endereco_web
    
# Modulo leitor tag  
def leitor_tag()->str:
    tag = input("Qual tag deseja encontrar na pagina? ")
    
    return tag


# Modulo leitor palavra
def leitor_palavra()->str:
    tag = input("Qual palavra deseja contar a quantidade no texto? ")
    
    return palavra

# Modulo impressora
def impressora(lista: list)-> None:
    titulo = lista[0]
    contagem = lista[1]
    
    print(f"O título do texto é: {titulo}")
    print(f"O numero de vezes que a tag escolhida aparece no texto é: {contagem}")