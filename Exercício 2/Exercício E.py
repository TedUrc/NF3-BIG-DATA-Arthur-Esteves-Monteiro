import pandas as pd
import numpy as np
import collections
from google.colab import files
import io

uploaded = files.upload()

tabela = pd.read_csv(io.BytesIO(uploaded['cursos-prouni.csv']))

# Exercício E
cursos_tecnologicos = []
for pos, x in tabela[['grau', 'curso_busca']].values:
  if 'tecnológico' in pos.strip().lower():
    cursos_tecnologicos.append((pos, x))
cursos_tecnologicos = pd.DataFrame(data=cursos_tecnologicos, columns=['grau', 'curso_busca'])
display(cursos_tecnologicos)