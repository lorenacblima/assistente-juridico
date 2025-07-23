from transformers import pipeline
import pandas as pd

print("✅ Iniciando classificação com LLM...")

try:
    # Carregando o dataset
    df = pd.read_csv("data/train_dataset.csv")
    print("✅ Dataset carregado com sucesso!")

    # Pegando os primeiros 50 textos e categorias reais
    textos = df["texto"].tolist()[:50]
    categorias_reais = df["categoria"].tolist()[:50]

    # Definindo as categorias possíveis
    labels = ["contrato", "petição", "sentenca", "jurisprudencia"]

    # Carregando o modelo de zero-shot
    print("📦 Carregando modelo 'facebook/bart-large-mnli'...")
    classificador = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    # Lista de resultados
    resultados = []

    # Rodando a classificação
    for i, (texto, real) in enumerate(zip(textos, categorias_reais)):
        resultado = classificador(texto, candidate_labels=labels)
        previsto = resultado["labels"][0]
        score = resultado["scores"][0]

        resultados.append({
            "texto": texto,
            "categoria_real": real,
            "categoria_prevista": previsto,
            "confianca": round(score, 4)
        })

        print(f"\n🔹 Texto {i+1}:")
        print(f"Real: {real}")
        print(f"Previsto: {previsto} (Confiança: {score:.4f})")

    # Salvando em CSV
    df_resultados = pd.DataFrame(resultados)
    df_resultados.to_csv("classifier/resultados_zero_shot.csv", index=False)
    print("\n✅ Resultados foram salvos em 'classifier/resultados_zero_shot.csv'")

except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")
