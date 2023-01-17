
from sklearn.datasets import load_iris
dados = load_iris()

import pandas as pd
# nessa primeira parte foi importado a função de dados pandas.
df = pd.DataFrame(dados.data)
df.columns = dados.feature_names
# já nessa segunda foi importado os dados referentes as plantas.
df['especiel'] = dados.target

df.describe()
# aqui eu pedide para ser descritos dados matemáticos sobre as plantas
df_0 = df.loc[df['especiel'] == 0]

df_1 = df.loc[df['especiel'] == 1]

df_2 = df.loc[df['especiel'] == 2]

sepal_length = df['sepal length (cm)']
sepal_width = df['sepal width (cm)']
petal_length = df['petal length (cm)']
petal_width = df['petal width (cm)']
import matplotlib.pyplot as plt
#função para importar variados tipos de gráficos
plt.bar(sepal_length, sepal_width, petal_length, petal_width)
#função para usar o gráfico scatter
plt.show()
#função para mostrar o gráfico no console

df.columns
#mostrar o nome das colunas

# As espécies tem o mesmo número de exemplares. A média da espécie sepal length
#é a maior média entre as espécies, seguido pela sepal width e com menor valor 
#de média é a espécie petal width. Já o desvio padrão tem como portador do 
#maior valor a espécie sepal length, seguido por sepal width e petal width. O 
#mínimo e máximo tem a mesma ordem em relação a portadores do maior valor, e   
# ordem é sepal length, sepal width e por último petal width.