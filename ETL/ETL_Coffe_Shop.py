# Carregamento Das Blibliotecas
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Carregamento de arquivos

#Escolhendo o caminho para o arquivo
path = 'ETL/Coffee Shop Sales.xlsx'

#Carregando o arquivo
data=pd.read_excel(path)

#Retirando tabelas inuteis para a gente
data = data.drop(columns=['transaction_id','transaction_time','transaction_date','product_id'] ,axis=1)

#Retirando dados nulos
data.dropna()

#Transformando os valores em tipos certos
data['transaction_qty'] = data['transaction_qty'].astype(int)
data['store_id'] = data['store_id'].astype(int)
data['unit_price'] = data['unit_price'].astype(float)
data[['store_location','product_category','product_type','product_detail']] = data[['store_location','product_category','product_type','product_detail']].astype(str)

#Agrupando os valores da tabela

data_agrupada = data.groupby(['store_id','store_location','product_category'],as_index=False )['transaction_qty'].sum()
data_agrupada

vendas_astoria =  data_agrupada[data_agrupada['store_id'] == 3]
vendas_manhattan =  data_agrupada[data_agrupada['store_id'] == 5]
vendas_kitchen =  data_agrupada[data_agrupada['store_id'] == 8]

vendas_astoria.to_excel('ETL/Vendas Astoria.xlsx',index=False)
vendas_manhattan.to_excel('ETL/Vendas Manhattan.xlsx',index=False)
vendas_kitchen.to_excel('ETL/Vendas Kitchen.xlsx',index=False)
data_agrupada.to_excel('ETL/Vendas Totais.xlsx', index=False)