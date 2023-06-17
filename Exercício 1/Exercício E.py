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

# Exercício E
# Parte -> 1
display(dataframe[['Year', 'Beverage Types']].loc[dataframe['Year'] == '1985'])

# Parte - 2
dataframe['Display Value'] = dataframe['Display Value'].replace(str(), 0).astype(float)
display(dataframe['Display Value'].loc[dataframe['Display Value'] > 4])