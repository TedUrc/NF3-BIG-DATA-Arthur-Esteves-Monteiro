import pandas as pd
import numpy as np
import collections
from google.colab import files
import io

uploaded = files.upload()

tabela = pd.read_csv(io.BytesIO(uploaded['cursos-prouni.csv']))

# Exercício F
tabela.drop(['cidade_filtro'], axis='columns', inplace=True)
display(tabela)