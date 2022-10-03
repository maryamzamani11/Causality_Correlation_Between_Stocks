from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
%matplotlib inline


start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2022, 1, 24)

# Import 27 of big US companies

tickers = ['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX','DIS','GS','HD','HON','IBM','INTC','JNJ','JPM','KO','MCD'
          ,'MRK','MMM','MSFT','NKE','PG','TRV','UNH','VZ','WBA','WMT']

Companies = [AAPL, AMGN, AXP, BA, CAT, CSCO, CVX, DIS, GS, HD, HON, IBM, INTC, JNJ, JPM, KO, MCD
          , MRK, MMM, MSFT, NKE, PG, TRV, UNH, VZ, WBA, WMT]

Companies = []
for company in tickers:
    Companies.append(data.DataReader(company, 'yahoo', start, end))

# Concatanate all the stocks into a single dataframe

Stocks = pd.concat(Companies,axis=1,keys=tickers)
Stocks.columns.names = ['Company Ticker','Stock Info']

# Make a dataframe with the log_return of the close prices

LogReturn_df = pd.DataFrame()

for ticker in tickers:
    LogReturn_df[ticker] = np.log(Stocks[ticker]['Close']).diff()
LogReturn_df.dropna(inplace=True) 

# Look for the dynamics of the correlation between stocks by considering a moving window with the size of 252 days and the step size of 63 days

Max_T = LogReturn_df.shape[0]
N=int(Max_T / 63)

Correlation_array = {}
Date_middle_moving_Window = []
Average_Corr = []

for i in range(N-1):
    Correlation_array[i]=LogReturn_df.iloc[i*63:252+i*63].corr()
    Date_middle_moving_Window.append(LogReturn_df.iloc[i*63:252+i*63].index[126]) # pick the data of the middle of the window
    Average_Corr.append(Correlation_array[i].mean().mean())

    
date_MeanCorr = list(zip(Date_middle_moving_Window,Average_Corr))  
df_ave_Corr = pd.DataFrame(date_MeanCorr, columns=['date','Corr'])  
df_ave_Corr=df_ave_Corr.set_index('date')

df_ave_Corr.plot(figsize=(14,6))
plt.show(


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# plot the heatmap of the correlation in two different time windows
fig, axes = plt.subplots(1, 2, figsize=(18, 6))
sns.heatmap(Correlation_array[76],xticklabels=tickers, yticklabels=tickers,ax=axes[0])
axes[0].set_title("2019/01/16 - 2020/01/15 ", size=14)

sns.heatmap(Correlation_array[77],xticklabels=tickers, yticklabels=tickers,ax=axes[1])
axes[1].set_title("2019/04/07 - 2020/04/16 ", size=14)

plt.savefig('Correlation_heatmap_USA.pdf')
plt.show()
