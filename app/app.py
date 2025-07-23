# app/app.py

import streamlit as st
import pandas as pd
import torch
import os
import json
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Configuração da página
st.set_page_config(page_title="Assistente Jurídico com IA", layout="centered")

# Título
st.title("📚 Assistente Jurídico com IA")
st.write("Classificador de textos jurídicos treinado com modelos da Hugging Face.")

# Carrega modelo e tokenizer com cache
@st.cache_resource
def load_model():
    model_path = "classifier/modelo_treinado"
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

model, tokenizer = load_model()

#  Função de classificação
def classificar_texto(texto):
    inputs = tokenizer(texto, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        confianca, pred = torch.max(probs, dim=1)
    return int(pred), float(confianca)

#  Carrega o mapeamento de rótulos
def carregar_labels():
    labels_path = os.path.join("classifier", "labels.json")
    with open(labels_path, "r", encoding="utf-8") as f:
        return json.load(f)

id2label = carregar_labels()

#  Modo de entrada
aba = st.radio("Escolha o modo de uso:", [" Texto Manual", " Upload CSV"])

#  Modo Texto Manual
if aba == " Texto Manual":
    texto = st.text_area("Digite o texto jurídico para classificar:", height=200)
    if st.button("Classificar"):
        if texto.strip() == "":
            st.warning("Por favor, insira um texto.")
        else:
            categoria, confianca = classificar_texto(texto)
            nome_categoria = id2label.get(str(categoria), "Desconhecida")

            st.success(f"📌 Categoria prevista: {nome_categoria}")
            st.info(f"🔍 Confiança: **{confianca:.2%}**")

#  Modo Upload CSV
elif aba == " Upload CSV":
    arquivo = st.file_uploader("Faça upload de um arquivo CSV com uma coluna chamada `texto`", type=["csv"])
    if arquivo:
        df = pd.read_csv(arquivo)

        if "texto" not in df.columns:
            st.error("O CSV deve conter uma coluna chamada `texto`.")
        else:
            resultados = []
            for texto in df["texto"]:
                categoria, confianca = classificar_texto(texto)
                nome_categoria = id2label.get(str(categoria), "Desconhecida")
                resultados.append({
                    "texto": texto,
                    "categoria": nome_categoria,
                    "confiança": f"{confianca:.2%}"
                })

            st.subheader(" Resultados da Classificação")
            st.dataframe(pd.DataFrame(resultados))
