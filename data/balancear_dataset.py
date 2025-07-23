# data/balancear_dataset.py

import pandas as pd
import os

def balancear_dataset(path_csv="data/dataset.csv", path_saida="data/dataset_balanceado.csv"):
    df = pd.read_csv(path_csv)

    # Conta quantas linhas há por categoria
    contagem = df["categoria"].value_counts()
    print("Contagem original por categoria:\n", contagem)

    # Encontra a menor quantidade entre as categorias
    menor_qtd = contagem.min()

    # Balanceia mantendo apenas a menor quantidade de cada categoria
    df_balanceado = df.groupby("categoria").sample(n=menor_qtd, random_state=42)

    # Embaralha as linhas
    df_balanceado = df_balanceado.sample(frac=1, random_state=42).reset_index(drop=True)

    # Salva o novo CSV
    df_balanceado.to_csv(path_saida, index=False, encoding="utf-8")
    print(f"\n Dataset balanceado salvo em {path_saida}")

if __name__ == "__main__":
    balancear_dataset()
