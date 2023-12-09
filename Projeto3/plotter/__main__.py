import design as des
import es

#Le a função escolhida
funcao = es.leitor_funcao()

# Se houver, le os coeficientes
if funcao == 1 or funcao == 2:
    coeficientes = es.leitor_coeficientes()

# Processa o grafico

if funcao == 1:
    valores = des.afim(coeficientes[0],coeficientes[1])
elif funcao == 2:
    valores = des.quadratica(coeficientes[0],coeficientes[1])
elif funcao == 3:
    valores = des.exponencial()
elif funcao == 4:
    valores = des.logaritmo()
else:
    print("Função digitada não existe")
    exit


# Imprime o gráfico da função
es.impressora(valores,funcao)