import pandas as pd
import numpy as np
import collections
from google.colab import files
import io

uploaded = files.upload()

tabela = pd.read_csv(io.BytesIO(uploaded['cursos-prouni.csv']))

# Exercício J
grau_nota_cotas = dict()
for pos, x in tabela[['grau', 'nota_integral_cotas']].values:
  if pos not in grau_nota_cotas:
    grau_nota_cotas.update({pos: x})
  elif pos in grau_nota_cotas:
    grau_nota_cotas[pos] += x
grau_nota_cotas = pd.DataFrame(data=grau_nota_cotas.items(),
                               columns=['grau', 'nota_integral_cotas'])
grau_nota_cotas.plot.bar(x='grau')