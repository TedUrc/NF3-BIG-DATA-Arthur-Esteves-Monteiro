import pandas as pd
import numpy as np
import collections
from google.colab import files
import io

uploaded = files.upload()

tabela = pd.read_csv(io.BytesIO(uploaded['cursos-prouni.csv']))

# Exercício B
grau = collections.Counter(tabela['grau'])
grau_dataframe = pd.DataFrame(data=grau.keys(), columns=['grau'])
display(grau_dataframe)