import pandas as pd
import matplotlib.pyplot as plt


# Ler CSV
df = pd.read_csv("bmw.csv")

# Limpeza
df = df.drop_duplicates()

# Maior Quilometragem 
max_mileage = df['mileage'].max()
print("Maior Quilometragem", max_mileage)

# Carro(s) com maior quilometragem
carros_max_mileage = df[df['mileage'] == max_mileage]
print(carros_max_mileage[['model', 'mileage', 'price']])

# Preço médio por modelo
preco_medio_modelo = df.groupby('model')['price'].mean().sort_values()

# converter em inteiro 
preco_medio_modelo = preco_medio_modelo.astype(int)
print(preco_medio_modelo)


# Criar gráfico de barras

plt.figure(figsize=(10,6))
preco_medio_modelo.plot(kind='bar', color='skyblue')
plt.title('Preço Médio por Modelo')
plt.xlabel('Modelo')
plt.ylabel('Preço Médio')
plt.xticks(ticks=range(len(preco_medio_modelo)), labels=preco_medio_modelo.index, rotation=45)

for i, row in carros_max_mileage.iterrows():
    modelo = row['model']
    preco = row['price']
    
    # Encontrar a posição do modelo no eixo x
    if modelo in list(preco_medio_modelo.index):
        x_pos = list(preco_medio_modelo.index).index(modelo)
        plt.annotate(f'Maior km: {row["mileage"]}',
                     xy=(x_pos, preco),
                     xytext=(0, preco + 2000),
                     textcoords='offset points',
                     arrowprops=dict(facecolor='red', arrowstyle='->'))

plt.tight_layout()
plt.show()
