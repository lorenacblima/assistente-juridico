import pandas as pd
import numpy as np
import torch
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
)

# 🔹 Lendo o CSV
print("🔹 Lendo o CSV...")
df = pd.read_csv("data/train_dataset.csv")

# 🔹 Codificando as categorias
print("🔹 Codificando as categorias...")
le = LabelEncoder()
df["label"] = le.fit_transform(df["categoria"])

# 🔹 Dividindo em treino e validação (80/20)
train_df, val_df = train_test_split(df[["texto", "label"]], test_size=0.2, random_state=42)

# 🔹 Convertendo para Dataset Hugging Face
print("🔹 Convertendo para Dataset...")
train_dataset = Dataset.from_pandas(train_df)
eval_dataset = Dataset.from_pandas(val_df)

# 🔹 Tokenizando
print("🔹 Tokenizando...")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def tokenize(example):
    return tokenizer(example["texto"], truncation=True, padding="max_length", max_length=256)

train_dataset = train_dataset.map(tokenize, batched=True)
eval_dataset = eval_dataset.map(tokenize, batched=True)

# 🔹 Carregando modelo
print("🔹 Carregando modelo...")
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", num_labels=len(le.classes_)
)

# 🔹 Configurando treinamento
print("🔹 Configurando treinamento...")
training_args = TrainingArguments(
    output_dir="classifier/modelo_treinado",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=10,
    weight_decay=0.01,
    logging_dir="classifier/logs",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="loss",
    greater_is_better=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

# 🔹 Treinando
trainer.train()

# 🔹 Salvando modelo e tokenizer
model.save_pretrained("classifier/modelo_treinado")
tokenizer.save_pretrained("classifier/modelo_treinado")

print("✅ Treinamento finalizado com sucesso!")

# Salvar modelo e tokenizer treinados
output_dir = "classifier/modelo_treinado"
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)
print(f"🔹 Modelo salvo em: {output_dir}")