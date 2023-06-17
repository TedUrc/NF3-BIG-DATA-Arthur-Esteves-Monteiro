import pandas as pd
import numpy as np
import collections
from google.colab import files
import io

uploaded = files.upload()

tabela = pd.read_csv(io.BytesIO(uploaded['cursos-prouni.csv']))

# Exercício I
cursos_bacharelado_ampla = dict()
for pos, x, y in tabela[['grau', 'curso_busca', 'nota_integral_ampla']].values:
  if pos.lower().strip() == 'bacharelado':
    if x not in cursos_bacharelado_ampla:
      cursos_bacharelado_ampla.update({x: [pos, y]})
    elif x in cursos_bacharelado_ampla:
      cursos_bacharelado_ampla[x][1] += y

keys = list(cursos_bacharelado_ampla.keys())
var = list(cursos_bacharelado_ampla.values())
valores= [(var[x][0], keys[x], var[x][1]) for x in range(len(keys))]
cursos_bacharelado_ampla = pd.DataFrame(data=valores,
                                        columns=['grau', 'curso_busca', 'nota_integral_ampla'])
display(cursos_bacharelado_ampla.describe())