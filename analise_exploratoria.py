
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
#ler o csv
dados = pd.read_csv('dados.csv')
#verifica se á dados duplicados
dados_dup = dados.duplicated().sum()
print(dados_dup)
print(dados)
#verifica valores Nulos
dados_null = dados.isnull().sum()
print(dados_null)
#Grafico para identificar Possiveis Outliers
sb.boxplot(dados)
plt.show()
#Maior valor empenhado comparo ao Pib
dados_empenho_max = dados.max()
print(f'Município com o maior valor empenhado:\n{dados_empenho_max}')
#Pib Menor que Valor empenhado
#retorna todos os municipios com Valor empenhado maior que o pib
pib_menor_que_empenho = dados['PIB'] < dados['VALOREMPENHO']
#quantidade de municipios com Possivel Ineficiencia de Recursos
quantidade_municipios = pib_menor_que_empenho.sum()
print(f'Quantidade de municipios com Possiveis Ineficiencias ou uso indevido de Recurssos:\n{quantidade_municipios}')
#Quais Municipios são
pib_menor_que_empenho = dados[pib_menor_que_empenho]
print(f'Municípios com possível ineficiência no uso dos recursos:\n{pib_menor_que_empenho}')
#Pib Maior que Valores empenhados
#retorna municipios com Pib maiores que Valores empenhados
pib_maior_que_empenho = dados['PIB'] > dados['VALOREMPENHO']
#Quantos municipios são
quantidade_municipios_pib = pib_maior_que_empenho.sum()
#Quais municipios são
pib_maior_que_empenho = dados[pib_maior_que_empenho]
print(f'Municípios com possível eficiência no uso dos recursos:\n{pib_maior_que_empenho}')
print(f'Quantidade de municipios com Possivel Eficiencia nos usos de Recursos:\n{quantidade_municipios_pib}')
#histograma Pib Maior que Valores empenhados
sb.histplot(pib_maior_que_empenho['PIB'], kde=True)

plt.title('Distribuição do PIB para Municípios com PIB maior que o Valor Empenhado')
plt.xlabel('PIB')
plt.ylabel('Frequência')
plt.show()
#Histograma com Pib Menores que Valores empenhados
sb.histplot(pib_menor_que_empenho['PIB'], kde=True)

plt.title('Distribuição do PIB para Municípios com PIB menor que o Valor Empenhado')
plt.xlabel('PIB')
plt.ylabel('Frequência')
plt.show()
#Grafico de dispersão Relação entre Pib e Valor empenhado
sb.scatterplot(x=dados['PIB'], y=dados['VALOREMPENHO'])

plt.title('Relação entre PIB e Valor Empenhado dos Municípios')
plt.xlabel('PIB')
plt.ylabel('Valor Empenhado')
plt.show()
#Relação entre PIB e Valor Empenhado com Regressão Linear
sb.regplot(x=dados['PIB'], y=dados['VALOREMPENHO'])

plt.title('Relação entre PIB e Valor Empenhado com Regressão Linear')
plt.xlabel('PIB')
plt.ylabel('Valor Empenhado')
plt.show()
#Cria uma Figura em Branco
plt.figure()
#Posições das Figuras/ Grafico
plt.subplot(2,2,1)
sb.histplot(pib_maior_que_empenho['PIB'], kde=True)
#Posições das Figuras/ Grafico
plt.subplot(2,2,2)
sb.histplot(pib_menor_que_empenho['PIB'], kde=True)
#Posições das Figuras/ Grafico
plt.subplot(2,2,3)
sb.scatterplot(x=dados['PIB'], y=dados['VALOREMPENHO'])
#Posições das Figuras/ Grafico
plt.subplot(2,2,4)
sb.regplot(x=dados['PIB'], y=dados['VALOREMPENHO'])

plt.show()









