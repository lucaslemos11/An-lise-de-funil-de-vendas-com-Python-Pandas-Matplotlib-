import pandas as pd

# carregar dados (com separador correto)
df = pd.read_csv('dados_funil.csv', sep=';')

# remover espaços invisíveis
df.columns = df.columns.str.strip()

# criar métricas
df['taxa_visitante_lead'] = df['leads'] / df['visitantes']
df['taxa_lead_venda'] = df['vendas'] / df['leads']

# mostrar tabela
print(df)

# médias
print("\nMédia visitante -> lead:", df['taxa_visitante_lead'].mean())
print("Média lead -> venda:", df['taxa_lead_venda'].mean())

import matplotlib.pyplot as plt

# gráfico de volume
df.plot(x='mes', y=['visitantes','leads','vendas'])
plt.title('Funil de Vendas - Volume')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_volume.png')
plt.show()

# gráfico de taxas
df.plot(x='mes', y=['taxa_visitante_lead','taxa_lead_venda'])
plt.title('Taxas de Conversão')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_taxas.png')
plt.show()