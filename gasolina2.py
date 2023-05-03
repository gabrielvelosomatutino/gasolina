import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

df = pd.read_csv('gasolina.csv')
df.head()

plt.figure(figsize=(15,8))
plt.plot(df['dia'], df['venda'], color = 'red')
plt.savefig('gasolina2.png')