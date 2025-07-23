# data/load_train_data.py

import csv
import random
from exemplos_reais import exemplos_por_categoria

def gerar_exemplos(categoria, quantidade):
    exemplos = exemplos_por_categoria[categoria]
    return [random.choice(exemplos) for _ in range(quantidade)]

def gerar_dataset_csv(path_csv="data/dataset.csv"):
    categorias = list(exemplos_por_categoria.keys())
    
    # Quantidade desbalanceada por categoria
    quantidades = {
        "contrato": 100,
        "petição": 50,
        "sentenca": 30,
        "jurisprudencia": 20
    }

    with open(path_csv, mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["texto", "categoria"])

        for categoria in categorias:
            textos = gerar_exemplos(categoria, quantidades[categoria])
            for texto in textos:
                writer.writerow([texto, categoria])
    
    print(f"✅ CSV gerado com sucesso em {path_csv}")

if __name__ == "__main__":
    gerar_dataset_csv()

