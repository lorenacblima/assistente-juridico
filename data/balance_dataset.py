import pandas as pd

# Caminho do dataset original
df = pd.read_csv("data/dataset.csv")

# Contar exemplos por categoria
print("Distribuição original:")
print(df['categoria'].value_counts())

# Limite por categoria
limite = 60

# Subamostrar categorias com mais de 60 exemplos
balance_dataset = df.groupby("categoria").apply(lambda x: x.sample(n=min(len(x), limite), random_state=42)).reset_index(drop=True)

# Salvar dataset balanceado
balance_dataset.to_csv("data/train_dataset.csv", index=False)

print("\nDistribuição após balanceamento:")
print(balance_dataset['categoria'].value_counts())

df = pd.read_csv("data/balance_dataset.csv")