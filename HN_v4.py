#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Health Nutrition And Population Statistics

dados = pd.read_csv("HNP_StatsData.csv", sep = ',')
dados.info()


# In[2]:


dados.head()


# In[3]:


df = sns.set(rc={'figure.figsize': (35,15)})
df = sns.heatmap(dados.isna(), cbar = False)
df = plt.subplots_adjust(bottom=0.25, top=.9)
df


# In[4]:


indicadores_unicos = dados["Indicator Name"].unique()
indicadores_unicos


# In[5]:


contagem_indicadores = len(indicadores_unicos)
contagem_indicadores


# In[6]:


paises_unicos = dados["Country Name"].unique()
paises_unicos


# In[7]:


contagem_paises = len(paises_unicos)
contagem_paises


# In[8]:


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


# In[9]:


# Criando BD para 2019

#paises = dados["Country Name"].unique()
#relatorio = list()
#for pais in paises:
#    linha_relatorio = [pais]
#    for indicador in selecao_geral:
#        df_temp = dados[(dados["Country Name"] == pais) & (dados["Indicator Name"] == indicador)]
#        valor = df_temp.iloc[0]["2019"]
#        linha_relatorio.append(valor)
#    relatorio.append(linha_relatorio)


# In[10]:


#Salvando BD de 2019

#colunas = ["Pais"]
#colunas.extend(selecao_geral)
#df_ind_2019 = pd.DataFrame(relatorio, columns=colunas)
#df_ind_2019.head()
#df_ind_2019.to_excel("Dados_2019.xlsx")


# In[11]:


df_ind_2019.head()


# In[12]:


#df_temp = dados[dados["Indicator Name"] == "Community health workers (per 1,000 people)"]


# In[13]:


#df_temp.info()


# In[14]:


# Criando BD para 2020

#paises = dados["Country Name"].unique()
#relatorio = list()
#for pais in paises:
#    linha_relatorio = [pais]
#    for indicador in selecao_geral:
#        df_temp = dados[(dados["Country Name"] == pais) & (dados["Indicator Name"] == indicador)]
#        valor = df_temp.iloc[0]["2020"]
#        linha_relatorio.append(valor)
#    relatorio.append(linha_relatorio)
    


# In[15]:


#Salvando BD de 2020

#colunas = ["Pais"]
#colunas.extend(selecao_geral)
#df_ind_2019 = pd.DataFrame(relatorio, columns=colunas)
#df_ind_2019.head()
#df_ind_2019.to_excel("Dados_2020.xlsx")


# In[16]:


#Criando BD para 2021

#paises = dados["Country Name"].unique()
#relatorio = list()
#for pais in paises:
#    linha_relatorio = [pais]
#    for indicador in selecao_geral:
#        df_temp = dados[(dados["Country Name"] == pais) & (dados["Indicator Name"] == indicador)]
#        valor = df_temp.iloc[0]["2021"]
#        linha_relatorio.append(valor)
#    relatorio.append(linha_relatorio)


# In[17]:


#Salvando BD de 2021

#colunas = ["Pais"]
#colunas.extend(selecao_geral)
#df_ind_2019 = pd.DataFrame(relatorio, columns=colunas)
#df_ind_2019.head()
#df_ind_2019.to_excel("Dados_2021.xlsx")


# In[18]:


#Criando BD para 2022

#paises = dados["Country Name"].unique()
#relatorio = list()
#for pais in paises:
#    linha_relatorio = [pais]
#    for indicador in selecao_geral:
#        df_temp = dados[(dados["Country Name"] == pais) & (dados["Indicator Name"] == indicador)]
#        valor = df_temp.iloc[0]["2022"]
#        linha_relatorio.append(valor)
#    relatorio.append(linha_relatorio)


# In[19]:


#Salvando BD de 2022

#colunas = ["Pais"]
#colunas.extend(selecao_geral)
#df_ind_2019 = pd.DataFrame(relatorio, columns=colunas)
#df_ind_2019.head()
#df_ind_2019.to_excel("Dados_2022.xlsx")


# In[20]:


df_2019 = pd.read_excel("Dados_2019.xlsx")
df_2019.info()
#PCA (analise de componentes principais)


# In[21]:


df_2019_limpa = df_2019.drop(columns=["Unnamed: 0"])
df_2019_limpa.head()


# In[22]:


df_2020 = pd.read_excel("Dados_2020.xlsx")
df_2020.info()


# In[23]:


df_2020_limpa = df_2020.drop(columns=["Unnamed: 0"])
df_2020_limpa.head()


# In[24]:


df_2021 = pd.read_excel("Dados_2021.xlsx")
df_2021.info()


# In[25]:


df_2021_limpa = df_2021.drop(columns=["Unnamed: 0"])
df_2021_limpa.head()


# In[26]:


df_2022 = pd.read_excel("Dados_2022.xlsx")
df_2022.info()


# In[27]:


df_2022_limpa = df_2022.drop(columns=["Unnamed: 0"])
df_2022_limpa.head()


# In[28]:


df_2019_limpa.describe().round(3)


# In[29]:


correlacoes = df_2019_limpa.corr()

sns.set(style="white")
plt.figure(figsize=(40, 30))
sns.heatmap(correlacoes, annot=True, cmap='coolwarm', linewidths=.5)

plt.show()


# In[ ]:




