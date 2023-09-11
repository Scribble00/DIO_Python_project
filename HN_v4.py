#O projeto ainda está em andamento, apenas algumas informações foram extraidas para compreender melhor a base que será trabalhada
#Serão incluídas ainda outras bases para dar suporte ao trabalho que será realizado
#Serão utilizadas técnicas de machine learning para tirar insights mais conclusivos


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Health Nutrition And Population Statistics
#Abrindo o arquivo CSV
dados = pd.read_csv("HNP_StatsData.csv", sep = ',')
dados.info()

#Primeiro contato com os dados
dados.head()

#Criando um gráfico para analisar dados faltantes
df = sns.set(rc={'figure.figsize': (35,15)})
df = sns.heatmap(dados.isna(), cbar = False)
df = plt.subplots_adjust(bottom=0.25, top=.9)
df

#Visualizando indicadores
indicadores_unicos = dados["Indicator Name"].unique()
indicadores_unicos

#Contando quantos indicadores únicos o DF possui
contagem_indicadores = len(indicadores_unicos)
contagem_indicadores

#Visualizando países e macroregiões presentes no DF
paises_unicos = dados["Country Name"].unique()
paises_unicos

#Contando quantos países e macroregiões únicas o DF possui
contagem_paises = len(paises_unicos)
contagem_paises

#Selecionando os indicadores que serão analisados
selecao_geral = [
"Birth rate, crude (per 1,000 people)",#taxa de natalidade por 1000 habitantes
"Current health expenditure (% of GDP)",#estima a quantidade de dinheiro gasta pelo pais
"Current health expenditure per capita (current US$)",
"Death rate, crude (per 1,000 people)",
"Domestic general government health expenditure (% of current health expenditure)",
"Domestic general government health expenditure (% of GDP)",
"Domestic general government health expenditure (% of general government expenditure)",
"Domestic general government health expenditure per capita (current US$)",
"Domestic general government health expenditure per capita, PPP (current international $)",
"Domestic private health expenditure (% of current health expenditure)",
"Domestic private health expenditure per capita (current US$)",
"External health expenditure (% of current health expenditure)",
"External health expenditure per capita (current US$)",
"GNI per capita, Atlas method (current US$)",
"Immunization, BCG (% of one-year-old children)",#tuberculose
"Immunization, DPT (% of children ages 12-23 months)",#triplice (difteria, tétano e coqueluche)
"Immunization, HepB3 (% of one-year-old children)",#hepatite B
"Immunization, Hib3 (% of children ages 12-23 months)",#meningite
"Immunization, measles (% of children ages 12-23 months)",#sarampo
"Immunization, measles second dose (% of children by the nationally recommended age)",#sarampo
"Immunization, Pol3 (% of one-year-old children)", #poliomelite
"Incidence of malaria (per 1,000 population at risk)",
"Incidence of tuberculosis (per 100,000 people)",
"Life expectancy at birth, total (years)",
"Newborns protected against tetanus (%)",
"Number of under-five deaths",
"Population growth (annual %)",
"Population, total",
"Prevalence of HIV, total (% of population ages 15-49)"
]

# Criando BD para o ano de 2019

paises = dados["Country Name"].unique()
relatorio = list()
for pais in paises:
   linha_relatorio = [pais]
   for indicador in selecao_geral:
       df_temp = dados[(dados["Country Name"] == pais) & (dados["Indicator Name"] == indicador)]
       valor = df_temp.iloc[0]["2019"]
       linha_relatorio.append(valor)
   relatorio.append(linha_relatorio)

#Salvando BD para o ano de 2019

colunas = ["Pais"]
colunas.extend(selecao_geral)
df_ind_2019 = pd.DataFrame(relatorio, columns=colunas)
df_ind_2019.head()
df_ind_2019.to_excel("Dados_2019.xlsx")

#checando informações para a base de dados criada
df_ind_2019.head()


# Criando BD para o ano de 2020

paises = dados["Country Name"].unique()
relatorio = list()
for pais in paises:
   linha_relatorio = [pais]
   for indicador in selecao_geral:
       df_temp = dados[(dados["Country Name"] == pais) & (dados["Indicator Name"] == indicador)]
       valor = df_temp.iloc[0]["2020"]
       linha_relatorio.append(valor)
   relatorio.append(linha_relatorio)

#Salvando BD para o ano de 2020

colunas = ["Pais"]
colunas.extend(selecao_geral)
df_ind_2019 = pd.DataFrame(relatorio, columns=colunas)
df_ind_2019.head()
df_ind_2019.to_excel("Dados_2020.xlsx")


#Criando BD para 2021

paises = dados["Country Name"].unique()
relatorio = list()
for pais in paises:
   linha_relatorio = [pais]
   for indicador in selecao_geral:
       df_temp = dados[(dados["Country Name"] == pais) & (dados["Indicator Name"] == indicador)]
       valor = df_temp.iloc[0]["2021"]
       linha_relatorio.append(valor)
   relatorio.append(linha_relatorio)


#Salvando BD de 2021

colunas = ["Pais"]
colunas.extend(selecao_geral)
df_ind_2019 = pd.DataFrame(relatorio, columns=colunas)
df_ind_2019.head()
df_ind_2019.to_excel("Dados_2021.xlsx")

#Criando BD para 2022

paises = dados["Country Name"].unique()
relatorio = list()
for pais in paises:
   linha_relatorio = [pais]
   for indicador in selecao_geral:
       df_temp = dados[(dados["Country Name"] == pais) & (dados["Indicator Name"] == indicador)]
       valor = df_temp.iloc[0]["2022"]
       linha_relatorio.append(valor)
   relatorio.append(linha_relatorio)


#Salvando BD de 2022

colunas = ["Pais"]
colunas.extend(selecao_geral)
df_ind_2019 = pd.DataFrame(relatorio, columns=colunas)
df_ind_2019.head()
df_ind_2019.to_excel("Dados_2022.xlsx")

#Descrevendo informações da base de dados de 2019
df_2019 = pd.read_excel("Dados_2019.xlsx")
df_2019.info()

#Limpando dados do DF de 2019
df_2019_limpa = df_2019.drop(columns=["Unnamed: 0"])
df_2019_limpa.head()

#Descrevendo informações da base de dados de 2020
df_2020 = pd.read_excel("Dados_2020.xlsx")
df_2020.info()

#Limpando dados do DF de 2020
df_2020_limpa = df_2020.drop(columns=["Unnamed: 0"])
df_2020_limpa.head()

#Descrevendo informações da base de dados de 2021
df_2021 = pd.read_excel("Dados_2021.xlsx")
df_2021.info()

#Limpando dados do DF de 2021
df_2021_limpa = df_2021.drop(columns=["Unnamed: 0"])
df_2021_limpa.head()

#Descrevendo informações da base de dados de 2022
df_2022 = pd.read_excel("Dados_2022.xlsx")
df_2022.info()

#Limpando dados do DF de 2022
df_2022_limpa = df_2022.drop(columns=["Unnamed: 0"])
df_2022_limpa.head()

#Analisando parâmetros da base de 2019
#Foi escolhida essa base por possuir o maior numero de valores relevantes
df_2019_limpa.describe().round(3)

#Fazendo a correlação entre os indicadores seleciondos
correlacoes = df_2019_limpa.corr()

#Plotando o Gráfico de correlação entre as varáveis
sns.set(style="white")
plt.figure(figsize=(40, 30))
sns.heatmap(correlacoes, annot=True, cmap='coolwarm', linewidths=.5)

plt.show()
