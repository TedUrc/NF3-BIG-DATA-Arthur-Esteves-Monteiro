import pandas as pd
import numpy as np
import collections
from google.colab import files
import io

uploaded = files.upload()

tabela = pd.read_csv(io.BytesIO(uploaded['cursos-prouni.csv']))

# Exercício H - Média das notas de corte dos cursos de tempo integral.
cursos_nota_ampla = dict()
for pos, x in tabela[['curso_busca', 'nota_integral_ampla']].values:
  if pos not in cursos_nota_ampla:
    cursos_nota_ampla.update({pos: [x, 1]})
  elif pos in cursos_nota_ampla:
    cursos_nota_ampla[pos][0] += x
    cursos_nota_ampla[pos][1] += 1
for pos, x in cursos_nota_ampla.items():
  cursos_nota_ampla.update({pos: x[0]/x[1]})
cursos_nota_ampla = pd.DataFrame(data=cursos_nota_ampla.items(),
                                 columns=['curso_busca', 'media_nota_ampla_integral'])
display(cursos_nota_ampla)
