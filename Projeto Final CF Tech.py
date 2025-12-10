import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as  sns

sns.set_theme(style="darkgrid")

# Definir a ação para análise.

ação = "ALPA3.SA"

# Baixar os dados de 12 meses usando yfinance.

dados = yf.download(ação, period = "1y")

# Verificar se os dados foram baixados corretamente. 

if dados.empty:
    print("Erro: Não foi possível baixar os dados. Verifique a sua internet ou o nome da ação.")
else:
    print("\n--- Dados baixados com sucesso. ---")

# Apresentar os resultados da análise.

dados.reset_index(inplace=True)
if isinstance(dados.columns, pd.MultiIndex):
    dados.columns = dados.columns.droplevel(1)

print("\n--- Tabela de Dados ---")
pd.set_option('display.max_columns', None) 
pd.set_option('display.width', 1000)
print(dados.head())

# Apresentar estatísticas.

print("\n--- Estatatísticas ---")
pd.options.display.float_format = '{:.2f}'.format
print(dados.describe(include=[np.number]))

#Verificar se há ausência de dados.

print("\n--- Ausência de dados ---")
print(dados.isnull().sum())

# Gráfico de linha do preço de fechamento.

plt.figure(figsize=(12, 6))
plt.plot(dados['Date'], dados['Close'])
plt.title(f'Preço de Fechamento - {ação}')
plt.xlabel('Data')
plt.ylabel('Preço (R$)')
plt.show()

# Gráfico de linha para o volume de negociações. 

plt.figure(figsize=(12, 6))
plt.plot(dados.index, dados['Volume'])
plt.title(f'Volume de negociações - {ação}')
plt.xlabel('Data')
plt.ylabel('Volume')
plt.show()

# Gráfico de dispersão entre os preços de negociações e de volume.

plt.figure(figsize=(12, 6))
plt.scatter(dados['Volume'], dados['Close'])
plt.title(f'Relação entre Preço de Fechamento e Volume - {ação}')
plt.xlabel('Volume')
plt.ylabel('Preço de Fechamento (R$)')
plt.show()

# Gráfico de média móvel.

import matplotlib.pyplot as plt

# Média móvel simples de 20 dias.

dados['SMA_20'] = dados['Close'].rolling(window=20).mean()

# Média móvel Exponencial de 50 dias.

dados['EMA_50'] = dados['Close'].ewm(span=50, adjust=False).mean()

plt.figure(figsize=(12, 6))
plt.plot(dados.index, dados['Close'], label='Preço de Fechamento')
plt.plot(dados.index, dados['SMA_20'], label='Média Móvel Simples 20d')
plt.plot(dados.index, dados['EMA_50'], label='Média Móvel Exponencial 50d')
plt.title(f'Preço de Fechamento e Médias Móveis - {ação}')
plt.xlabel('Data')
plt.ylabel('Preço (R$)')
plt.legend()
plt.show()

# Cálculo de retornos diários e volatilidade.

dados['Returns'] = dados['Close'].pct_change()
dados['Volatility'] = dados['Returns'].rolling(window=21).std() * np.sqrt(252)


# Histograma de retornos diários.

plt.figure(figsize=(12, 6))
sns.histplot(dados['Returns'].dropna(), kde=True)
plt.title(f'Histograma de Retornos Diários - {ação}')
plt.xlabel('Retorno Diário (%)')
plt.ylabel('Frequência (Quantidade de Dias)')
plt.legend()
plt.show()

# Análise de tendencias.

print("\n--- Análise de Tendências ---")

# Encontramos o primeiro e o ultimo preço.

primeiro_preco = dados['Close'].iloc[0]
ultimo_preco = dados['Close'].iloc[-1]

# Calculamos a porcentagem.

variacao_percentual = ((ultimo_preco - primeiro_preco) / primeiro_preco) * 100

# Mostramos o resultado.

print(f"Preço Inicial: R$ {primeiro_preco:.2f}")
print(f"Preço Final:   R$ {ultimo_preco:.2f}")
print(f"Variação no período: {variacao_percentual:.2f}%")

if variacao_percentual > 0:
    print("RESULTADO: Tendência de ALTA.")
else:
    print("RESULTADO: Tendência de BAIXA.")

# Análise de volume

print('\n--- Análise de Volume ---')

volume_medio = dados['Volume'].mean()
dias_alto_volume = dados[dados['Volume'] > volume_medio * 1.5]
print(f"Volume Médio Diário: {volume_medio:,.0f}")
print(f"Dias de Alto Volume: {len(dias_alto_volume)}")

print("Interpretação:")
if len(dias_alto_volume) > 5:
    print(f"Houve {len(dias_alto_volume)} dias de volume muito alto.")
    print("Isso indica forte participação institucional no ativo recente.")
else:
    print("O volume se manteve estável.")

# Conclusão da Análise da Ação

print("\n--- Conclusão ---")

print(f"A análise da ação {ação} nos últimos 12 meses nos mostra:")
print(f"1. Uma variação de {variacao_percentual:.2f}% no preço.")
media_volatilidade = dados['Volatility'].mean() * 100
print(f"2. Volatilidade média anualizada de {media_volatilidade:.2f}% (Risco).")
print(f"3. {len(dias_alto_volume)} dias com ALTO volume de negociação.")

if variacao_percentual > 0 and media_volatilidade < 40:
    print("RESULTADO: Ativo em tendência de alta com risco controlado. Temos um Cenário favorável.")
elif variacao_percentual > 0 and media_volatilidade >= 40:
    print("RESULTADO: Ativo subiu, mas com muita oscilação. Cuidado com a volatilidade.")
else:
    print("RESULTADO: Ativo em baixa. Momento exige cautela ou estratégia de venda.")