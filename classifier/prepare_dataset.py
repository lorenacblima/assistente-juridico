from datasets import Dataset
import pandas as pd

# Lendo o dataset balanceado
#df = pd.read_csv("data/dataset_balanceado.csv") 
df = pd.read_csv("data/dataset_balanceado.csv")

# Garantindo que os campos sejam string
df["texto"] = df["texto"].astype(str)
df["categoria"] = df["categoria"].astype(str)

# Convertendo para formato Hugging Face
dataset = Dataset.from_pandas(df)

# Salvando no disco
dataset.save_to_disk("data/hf_dataset")

print("✅ Dataset convertido e salvo com sucesso em: data/hf_dataset")
