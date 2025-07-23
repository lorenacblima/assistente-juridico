# classifier/inference.py

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import json

# Carrega os rótulos legíveis
with open("classifier/labels.json", "r", encoding="utf-8") as f:
    id2label = json.load(f)

# Carrega modelo e tokenizer
model = AutoModelForSequenceClassification.from_pretrained("classifier/modelo_treinado")
tokenizer = AutoTokenizer.from_pretrained("classifier/modelo_treinado")

def prever_categoria(texto):
    inputs = tokenizer(texto, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    predicted_class_id = torch.argmax(outputs.logits, dim=1).item()
    return id2label[str(predicted_class_id)]

if __name__ == "__main__":
    texto_exemplo = "Cláusula contratual que determina as obrigações das partes envolvidas."
    categoria = prever_categoria(texto_exemplo)
    print(f" Texto: {texto_exemplo}")
    print(f" Categoria prevista: {categoria}")

