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

# Exercício A - Agrupe os dados por tipo de bebidas;
bebidas = collections.Counter(dataframe['Beverage Types'])
bebidas_dataframe = pd.DataFrame(data=bebidas.keys(),
                                 columns=['Beverage Types'])
display(bebidas_dataframe)