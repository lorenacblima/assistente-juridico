# data/gerar_dataset_realista.py

import csv
import random
import os

# ⚖️ Distribuição mais realista entre as categorias
quantidades = {
    "contrato": 80,
    "petição": 60,
    "sentenca": 40,
    "jurisprudencia": 20
}

exemplos_reais = {
    "contrato": [
        "As partes resolvem firmar o presente contrato de prestação de serviços, com cláusulas claras e definidas.",
        "Fica estipulado que o pagamento será efetuado até o quinto dia útil de cada mês.",
        "O presente instrumento vigorará por 12 (doze) meses, podendo ser renovado automaticamente.",
        "Ambas as partes comprometem-se a manter sigilo sobre todas as informações comerciais tratadas neste contrato.",
        "As cláusulas contratuais só poderão ser alteradas mediante termo aditivo assinado por ambas as partes."
    ],
    "petição": [
        "Requer-se a concessão da justiça gratuita nos termos da Lei 1.060/50.",
        "Vem, respeitosamente, à presença de Vossa Excelência requerer a tutela antecipada.",
        "O autor não possui condições financeiras de arcar com as custas processuais.",
        "Conforme prova documental em anexo, o direito do requerente está devidamente demonstrado.",
        "Por todo o exposto, requer-se a citação do réu para responder aos termos da presente ação."
    ],
    "sentenca": [
        "Julgo procedente o pedido inicial para condenar o réu ao pagamento das verbas rescisórias.",
        "Diante da ausência de contestação, decreta-se a revelia da parte requerida.",
        "Homologo o acordo celebrado entre as partes para que produza os efeitos legais.",
        "A presente sentença resolve o mérito nos termos do artigo 487, I, do CPC.",
        "Determino a expedição de alvará judicial em favor da parte autora."
    ],
    "jurisprudencia": [
        "A jurisprudência do STJ é pacífica no sentido de admitir a penhora de bem de família em caso de fiança locatícia.",
        "O réu agiu com negligência ao prestar o serviço, causando dano à parte autora. O nexo causal entre a negligência e o prejuízo ficou comprovado.",
        "TJSP: 'A responsabilidade do fornecedor é objetiva, conforme prevê o Código de Defesa do Consumidor'.",
        "Havendo comprovação da relação de consumo, incide a inversão do ônus da prova.",
        "A Segunda Turma reconheceu a repercussão geral do tema para uniformizar o entendimento nos tribunais inferiores."
    ]
}

def gerar_exemplos(categoria, quantidade):
    exemplos = exemplos_reais[categoria]
    return [random.choice(exemplos) for _ in range(quantidade)]

def gerar_dataset(path_csv="data/dataset.csv"):
    os.makedirs("data", exist_ok=True)
    with open(path_csv, mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["texto", "categoria"])

        for categoria, quantidade in quantidades.items():
            textos = gerar_exemplos(categoria, quantidade)
            for texto in textos:
                writer.writerow([texto, categoria])
    
    print(f"Dataset realista gerado com sucesso em {path_csv}")

if __name__ == "__main__":
    gerar_dataset()
