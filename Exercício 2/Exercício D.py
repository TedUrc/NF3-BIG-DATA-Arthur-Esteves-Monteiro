import pandas as pd
import numpy as np
import collections
from google.colab import files
import io

uploaded = files.upload()

tabela = pd.read_csv(io.BytesIO(uploaded['cursos-prouni.csv']))

# Exercício D - Agrupe os dados por Estado e obtenha a média de notas de corte por Estado.
estados_notas = dict()
x = y = z = b = 0
for uf, nIA, nPA, nIC, nPC in tabela[['uf_busca', 'nota_integral_ampla', 'nota_parcial_ampla', 'nota_integral_cotas', 'nota_parcial_cotas']].values:
    if uf not in estados_notas:
        if nIA > 0:
            x = 1
        if nPA > 0:
            y = 1
        if nIC > 0:
            z = 1
        if nPC > 0:
            b = 1
        estados_notas.update({uf:[nIA, nPA, nIC, nPC, x, y, z, b]})
    elif uf in estados_notas:
        if estados_notas[uf][0] > 0:
            estados_notas[uf][0] += nIA
            estados_notas[uf][4] += 1
        if estados_notas[uf][1] > 0:
            estados_notas[uf][1] += nPA
            estados_notas[uf][5] += 1
        if estados_notas[uf][2] > 0:
            estados_notas[uf][2] += nIC
            estados_notas[uf][6] += 1
        if estados_notas[uf][2] > 0:
            estados_notas[uf][3] += nPC
            estados_notas[uf][7] += 1
keys = list(estados_notas.keys())
var = list(estados_notas.values())
valores = [(keys[x], var[x][0] / var[x][4], var[x][1] / var[x][5], var[x][2] / var[x][6], var[x][3] / var[x][7]) for x in range(len(keys))]
estados_notas = pd.DataFrame(data=valores,
                             columns=['uf_busca', 'media_integral_ampla', 'media_parcial_ampla', 'media_integral_cotas', 'media_parcial_cotas'])
display(estados_notas)