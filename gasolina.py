import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):
  
  grafico_gasolina = sns.lineplot(data=gasolina_df,x="dia", y="venda", palette='pastel')
  grafico_gasolina.set(title='Venda da gasolina na cidade de São Paulo nos 10 primeiros dias de Julho de 2021.', xlabel='Dia', ylabel='Preço');
plt.savefig('gasolina.png')