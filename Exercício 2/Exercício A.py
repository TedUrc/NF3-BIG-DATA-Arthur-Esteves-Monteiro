import pandas as pd
import numpy as np
import collections
from google.colab import files
import io

uploaded = files.upload()

tabela = pd.read_csv(io.BytesIO(uploaded['cursos-prouni.csv']))

# Exercício A
tabela[['bolsa_integral_cotas',
       'bolsa_integral_ampla', 'bolsa_parcial_cotas',
       'bolsa_parcial_ampla', 'nota_integral_ampla',
       'nota_integral_cotas', 'nota_parcial_ampla', 'nota_parcial_cotas']] = tabela[['bolsa_integral_cotas',
       'bolsa_integral_ampla', 'bolsa_parcial_cotas',
       'bolsa_parcial_ampla', 'nota_integral_ampla',
       'nota_integral_cotas', 'nota_parcial_ampla', 'nota_parcial_cotas']].replace(np.nan, 0.0)
display(tabela)
