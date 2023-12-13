import es
import proc

# Pega a URL e transforma em df

url = es.get_url()
dados = es.leitor_dados(url)

# Lista as colunas existentes

proc.colunas_existentes(dados)

# Define qual a coluna que deseja analisar

coluna = es.coluna_desejada()

# Calcula as estatísticas

estatisticas = proc.calcula_estatisticas(dados,coluna)

# Plota o gráfico da coluna desejada
es.plotter(dados,coluna)

# Imprime as estatisticas
es.imprime_estatistica(estatisticas)