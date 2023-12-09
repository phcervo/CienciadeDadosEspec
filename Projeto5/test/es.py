import os.path


# Funçao leitora de pagina

def leitor_pagina() -> str:
    pagina = input("Digite a URL que deseja baixar o conteúdo: ")
    return pagina

# Função impressora e geradora do arquivo.

def impressora(codigo_fonte) -> None:
    local_arquivo = input("Digite o local que deseja salvar o arquivo. (Se deixar vazio irá salvar na pasta de downloads.) : ")
    nome_arquivo = input("Digite o nome do arquivo .txt que deseja salvar: ")

    user_path = os.path.expanduser('~')
    download_path = user_path + '\\Downloads\\'

    if local_arquivo == '':
        nome_final = download_path + nome_arquivo + '.json'
    else:
        nome_final= user_path + local_arquivo + nome_arquivo + '.json'


    with open(nome_final, 'w',encoding="utf-8") as arquivo:
        arquivo.write(codigo_fonte)

    print(f"Arquivo salvo na pasta: {nome_final}")
    print('\n')
    #print(f'O código fonte da pagina é: {codigo_fonte}')