import matplotlib.pyplot as plt
import os
import pandas as pd

# Definir o caminho para os dados

DATA_PATH = os.environ.get('DATA_PATH')

# Dados fictícios
dados = {'categorias': ['A', 'B', 'C', 'D', 'E'],
         'valores': [1, 2, 3, 4, 5]}
df = pd.DataFrame(dados)

# Gerar o gráfico de barras
plt.bar(df["categorias"], df["valores"])
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')

# Mostrar o gráfico
plt.show()
