import pandas as pd
import numpy as np
import collections
from google.colab import files
import io

uploaded = files.upload()

tabela = pd.read_csv(io.BytesIO(uploaded['cursos-prouni.csv']))

# Exercício G
mensalidade = 0
num = 0
for x, z in tabela[['curso_busca', 'mensalidade']].values:
    if 'medicina' == x.lower().strip():
        mensalidade += z
        if z > 0:
            num += 1
media = mensalidade / num
print(f"Média da mensalidade do curso de Medicina: {media:.2f}R$")