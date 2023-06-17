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

# Exercício B
ano_regiao_dataframe = pd.DataFrame(data=dataframe[['Year', 'WHO region']],
                                    columns=['Year', 'WHO region'])
display(ano_regiao_dataframe)