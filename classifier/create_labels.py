import json

labels = {
    "0": "Contrato",
    "1": "Petição",
    "2": "Sentenca",
    "3": "Jurisprudencia"
}

with open("classifier/labels.json", "w", encoding="utf-8") as f:
    json.dump(labels, f, ensure_ascii=False, indent=4)

print("labels.json criado com sucesso!")
