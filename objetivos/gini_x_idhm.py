import matplotlib.pyplot as plt
import pandas as pd

#lendo o csv e obtendo um dataframe df
df = pd.read_csv("../dataBase_vulnerabilidade.csv", sep=";", engine="python", encoding='latin-1')

#Criando um novo Dataframe apenas com as colunas desejadas
colunas_solucao_1 = ['nome_uf', 'idhm_educ', 'i_gini']
df_solucao1 = df.loc[:, colunas_solucao_1]

#Convertendo colunas idhm_educ e i_gini para float
df_solucao1['idhm_educ'] = df_solucao1['idhm_educ'].str.replace(',', '.').astype(float)
df_solucao1['i_gini'] = df_solucao1['i_gini'].str.replace(',', '.').astype(float)

#filtrando colunas
df_solucao1 = df_solucao1[
    (df['nome_uf'] != '-') &
    (df['idhm_educ'] != 0) &
    (df['i_gini'] != 0)
]

#Criando um novo dataframe agrupado por nome dos estados
df_estado_idhm_gini = df_solucao1.groupby('nome_uf').mean()

#Obtendo resultados desejados
df_solucao1_idhmEduc = df_estado_idhm_gini.sort_values('idhm_educ')
df_solucao1_gini = df_estado_idhm_gini.sort_values('i_gini')
df_idhm_gini_orderByGini = df_estado_idhm_gini.sort_values('i_gini')

#Imprimindo resultados
print("10 Estados com menor IDHM Educacional do Brasil")
print(df_solucao1_idhmEduc.head(10))

print("\n10 Estados do Brasil com Indicadores Gini mais altos")
print(df_solucao1_gini.head(10))

print("\nlista de IDHM e Gini de cada estado do Brasil. Ordenado por estados menos desiguais")
print(df_idhm_gini_orderByGini)

