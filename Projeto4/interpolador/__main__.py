import es
import interpol

# Le as coordenadas
pontos=es.leitor_pontos()
f=interpol.ajusta_curva(pontos)

es.plota_grafico(pontos,f)