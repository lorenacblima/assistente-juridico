import pandas as pd
from faker import Faker
fake = Faker('pt_BR')

# Configurações
CATEGORIAS = {
    'contrato': [
        "CONTRATO DE {tipo} entre {partes} pelo prazo de {prazo}",
        "CLAÚSULA {n}: {obrigacao} sob pena de {pena}"
    ],
    'petição': [
        "EXCELENTÍSSIMO(A) {juiz}, {advogado} requer {pedido}",
        "PETIÇÃO INICIAL - {tipo}: Fundada no {lei}, pleiteia-se {acao}"
    ],
    'decisao_judicial': [
        "{tipo}: {decisao} com fundamento no {artigo}",
        "VISTOS. DECIDO: {decisao}"
    ],
    'lei': [
        "Art. {artigo}º: {texto}",
        "§ {paragrafo}. {complemento}"
    ]
}

# Gerador de dados
def gerar_linha(categoria):
    template = fake.random_element(CATEGORIAS[categoria])
    return template.format(
        tipo=fake.random_element(['LOCAÇÃO', 'PRESTAÇÃO DE SERVIÇOS', 'COMPRA E VENDA']),
        partes=fake.random_element(['LOCADOR e LOCATÁRIO', 'CONTRATANTE e CONTRATADA']),
        prazo=f"{fake.random_int(12, 60)} meses",
        n=fake.random_int(1, 20),
        obrigacao=fake.sentence(),
        pena=fake.random_element(['multa de 3 salários', 'rescisão contratual']),
        juiz=fake.random_element(['Juiz Federal', 'Juíza de Direito']),
        advogado=f"Dr.(a) {fake.name()}, OAB/{fake.random_int(10000, 99999)}",
        pedido=fake.random_element(['citação do réu', 'produção de prova pericial']),
        lei=fake.random_element(['art. 5º da CF', 'Lei 8.078/90']),
        acao=fake.random_element(['indenização por danos morais', 'reintegração de posse']),
        artigo=fake.random_element(['art. 333 do CPC', 'art. 186 do CC']),
        decisao=fake.random_element(['DEFIRO o pedido liminar', 'NEGO PROVIMENTO ao recurso']),
        texto=fake.sentence(),
        paragrafo=fake.random_int(1, 5),
        complemento=fake.sentence()
    )

# Geração do dataset
data = []
for categoria in CATEGORIAS:
    data.extend([{'text': gerar_linha(categoria), 'category': categoria} for _ in range(50)])

pd.DataFrame(data).to_csv("dataset_completo.csv", index=False)
print("✅ Dataset com 200 linhas gerado em dataset_completo.csv")