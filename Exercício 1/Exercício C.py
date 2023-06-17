import pandas as pd
import numpy as np
import collections
from google.colab import files
import io

uploaded = files.upload()

arquivo = pd.read_csv(io.BytesIO(uploaded['world_alcohol.csv']), sep=";")
colunas = arquivo.columns[0].split(",")
data = [x[0].split(',') for x in arquivo.values]

dataframe = pd.DataFrame(data=data, columns=colunas)
colunas.clear()
data.clear()

# Exercício C
contagem_regiao = collections.Counter(dataframe['WHO region'])
contagem_valores_bebidas = sum((dataframe['Display Value'].replace(str(), '0')).astype(float))
contagem_paises = collections.Counter(dataframe['Country'])
dataframe_secao_regiao = pd.DataFrame(data=contagem_regiao.items(), columns=["WHO region",
                                                 "Amount Region"])
dataframe_secao_paises = pd.DataFrame(data=contagem_paises.items(), columns=["Country",
                                                                     "Amount Country"])
dataframe_secao_soma = pd.DataFrame(data=[contagem_valores_bebidas], columns=["Sum of Display Value"])
display(dataframe_secao_regiao)
display(dataframe_secao_paises)
display(dataframe_secao_soma)