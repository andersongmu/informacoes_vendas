import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Produto': ['A', 'B', 'C', 'D'],
    'Preço Unitário': [10, 20, 15, 30],
    'Quantidade': [5, 3, 4, 2]
}
df = pd.DataFrame(dados)

df['Valor Total'] = df['Preço Unitário'] * df['Quantidade']

soma_valores_totais = df['Valor Total'].sum()

df.plot(x='Produto', y=['Preço Unitário', 'Quantidade', 'Valor Total'], kind='bar', figsize=(10, 6))
plt.xlabel('Produto')
plt.ylabel('Valor')
plt.title('Informações de Vendas')
plt.legend(['Preço Unitário', 'Quantidade', 'Valor Total'])

plt.text(df.shape[0], soma_valores_totais, f'Valor Total: {soma_valores_totais}', ha='center')

plt.show()