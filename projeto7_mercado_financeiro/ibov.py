# import yfinance as yf
# import pandas as pd
# import numpy as np

# tickers_IBOV = ["RADL3", "BRML3", "QUAL3", "ELET3", "BBDC3", "CCRO3", "BBSE3", "JBSS3", "ENBR3", "MRVE3", "ASAI3", "CRFB3", "TOTS3", "GGBR4", "TIMS3", "IRBR3", "USIM5", "BRFS3", "BBDC4", "BRAP4", "ABEV3", "UGPA3", "PETR3", "VBBR3", "BPAC11", "ITSA4", "BPAN4", "CSAN3", "DXCO3", "TAEE11", "PCAR3", "CIEL3", "RENT3", "PRIO3", "EGIE3", "HAPV3", "LWSA3", "LREN3", "FLRY3", "CPLE6", "RRRP3", "ALPA4", "CASH3", "COGN3", "ENGI11", "VALE3", "PETZ3", "SUZB3", "EMBR3", "MRFG3", "KLBN11", "AZUL4", "CMIN3", "AMER3", "ELET6", "BRKM5", "BEEF3", "CSNA3", "MGLU3", "SLCE3", "PETR4", "POSI3", "GOLL4", "SBSP3", "CYRE3", "EQTL3", "RDOR3", "GOAU4", "WEGE3", "ECOR3", "ARZZ3", "NTCO3", "CPFE3", "IGTI11", "EZTC3", "B3SA3", "CMIG4", "RAIL3", "RAIZ4", "HYPE3", "ITUB4", "ENEV3", "BBAS3", "VIIA3", "CVCB3", "SOMA3", "VIVT3", "MULT3", "SMTO3", "YDUQ3", "SANB11"]
# tickers_IBOV.sort()
# tickers_IBOV_SA = [i + '.SA' for i in tickers_IBOV]

# cotacoes_ibov = yf.download(tickers_IBOV_SA, start = '2021-01-01', period = "1d")

# cotacoes_ibov_longo = pd.melt(cotacoes_ibov, ignore_index = False)

# papeis = ['AMER3.SA', 'B3SA3.SA', 'BBDC4.SA', 'HAPV3.SA', 'PETR4.SA', 'RAIZ4.SA', 'PETR3.SA',
#           'VALE3.SA', 'IRBR3.SA', 'MGLU3.SA']

# df = cotacoes_ibov_longo[cotacoes_ibov_longo['Ticker'].isin(papeis)]

# petr = cotacoes_ibov.loc[:, cotacoes_ibov.columns.get_level_values('Ticker') == 'PETR4.SA']
# petr.columns = petr.columns.droplevel('Ticker')

import yfinance as yf
import pandas as pd

papeis = ['AMER3.SA', 'B3SA3.SA', 'BBDC4.SA', 'HAPV3.SA', 'PETR4.SA', 'RAIZ4.SA', 'PETR3.SA',
          'VALE3.SA', 'IRBR3.SA', 'MGLU3.SA']

cotacoes_ibov = yf.download(papeis, start='2021-08-04', period="1d")

# Melt the DataFrame and reset the index
df = pd.melt(cotacoes_ibov, ignore_index=False)
df["Date"] = df.index.date

df.reset_index(drop=True, inplace=True)

# Pivot the DataFrame to transform 'Price' values into columns
df_pivoted = df.pivot(index=["Date", "Ticker"], columns="Price", values="value").reset_index()
df_pivoted.iloc[:, 2:] = df_pivoted.iloc[:, 2:].applymap(lambda x: f"{x:.2f}".replace('.', ','))

# Rename the columns for clarity (optional)
df_pivoted.columns.name = None  # Remove the multi-index column name

print(df_pivoted)

