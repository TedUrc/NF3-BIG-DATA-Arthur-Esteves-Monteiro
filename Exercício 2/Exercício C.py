import pandas as pd
import numpy as np
import collections
from google.colab import files
import io

uploaded = files.upload()

tabela = pd.read_csv(io.BytesIO(uploaded['cursos-prouni.csv']))

# Exercício C - Agrupe os dados pelos cursos de Matemática, Medicina e Pedagogia.
curso = dict()
for x in tabela['curso_busca']:
    if x.lower().strip() == 'matemática':
        if x not in curso:
          curso.update({x: 1})
        else:
          curso[x] += 1
    elif x.lower().strip() == 'medicina':
        if x not in curso:
          curso.update({x: 1})
        else:
          curso[x] += 1
    elif x.lower().strip() == 'pedagogia':
        if x not in curso:
          curso.update({x: 1})
        else:
          curso[x] += 1
curso_dataframe = pd.DataFrame(data=curso.items(),
                               columns=['curso_busca', 'quantidade_curso'])
display(curso_dataframe)