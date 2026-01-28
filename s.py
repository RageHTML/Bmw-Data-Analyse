import pandas as pd

df = pd.read_csv("bmw.csv")

variables = ["price", "mileage", "engineSize", "tax"]
df_selected = df[variables]

correlation_matrix = df_selected.corr(method="pearson")

print("Matriz de Correlação de Pearson:\n")
print(correlation_matrix)

print("\nCorrelação com o preço:")
print("Mileage x Price:", correlation_matrix.loc["mileage", "price"])
print("EngineSize x Price:", correlation_matrix.loc["engineSize", "price"])
print("Tax x Price:", correlation_matrix.loc["tax", "price"])
