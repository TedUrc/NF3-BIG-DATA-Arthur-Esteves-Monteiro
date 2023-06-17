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

# Exercício D - Realize análises estatísticas da coluna dos valores: Média, Moda, Mediana, Estatística Descritiva e Gráfico de comparação dos valores agrupados por tipo de bebida.
media = dataframe['Display Value'].replace(str(), '0').astype(float).mean()
moda = dataframe['Display Value'].replace(str(), '0').astype(float).mode()[0]
mediana = dataframe['Display Value'].replace(str(), '0').astype(float).median()
print(f'Média do Display Value: {media}')
print(f'Moda do Display Value: {moda}')
print(f'Mediana do Display Value: {mediana}')
result = dataframe['Display Value'].replace(str(), 0).astype(float)
display(result.describe())
result = collections.Counter(dataframe['Beverage Types'])
result = pd.DataFrame(data=result.items(), columns=["Beverage Types", "Amount Beverage"])
result.plot.bar(x='Beverage Types')