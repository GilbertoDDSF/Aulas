# importar base de dados

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tabela = pd.read_csv(r"C:\Users\Gilberto\OneDrive\Área de Trabalho\Aula\Aula4\advertising.csv")
print(tabela)

print(tabela.corr())
#
sns.heatmap(tabela.corr(), annot=True, cmap="Wistia")
plt.show()
#
# y = quem voce quer prever (vendas)
# x = o que voce quer testar na base de dados

y = tabela["Vendas"]
x = tabela[["Tv", "Radio", "Jornal"]]

print(x)
print(y)
from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

print("IA")
modelo_regressaolinear = LinearRegression()
modelo_arvorededecisao = RandomForestRegressor()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvorededecisao.fit(x_treino, y_treino)

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvorededecisao = modelo_arvorededecisao.predict(x_teste)

from sklearn.metrics import r2_score

print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvorededecisao))
