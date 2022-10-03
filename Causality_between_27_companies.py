from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
%matplotlib inline
from statsmodels.tsa.stattools import grangercausalitytests, adfuller


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





#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Look for Granger causality interaction between stocks in different time windows
Max_T = LogReturn_df.shape[0]
N=int(Max_T / 63)
maxlag=5
test = 'ssr_chi2test'
Causal_p_Matrix={}

for l in range(N-1):
    Causal_p_Matrix[l]=np.zeros((27,27))
    
    df=LogReturn_df.iloc[l*63:252+l*63]
    
    for i in range(27):
        comp1 = tickers[i]
        for j in range(27):
            comp2 = tickers[j]
            gc_res=grangercausalitytests(df[[comp1,comp2]],maxlag, verbose=False);
            p_values = [round(gc_res[k+1][0][test][1],4) for k in range(maxlag)];
            min_p_value = np.min(p_values);
            Causal_p_Matrix[l][i][j]=min_p_value;
            

Causal_Matrix={}
for l in range(N-1):            
    Causal_Matrix[l]=np.zeros((27,27))
    for i in range(27):
        for j in range(27):
            if Causal_p_Matrix[l][i][j]<0.05:
                Causal_Matrix[l][i][j]=1
            else:
                Causal_Matrix[l][i][j]=0              
            
Date = []
Mean_causality=[]
for l in range(N-1):    
    Date.append(LogReturn_df.iloc[l*63:252+l*63].index[126])
    Mean_causality.append(np.mean(Causal_Matrix[l]))            
            
            
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# plot the heatmap of the causality matrix in two different time windows
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
sns.heatmap(Causal_Matrix[76],xticklabels=tickers, yticklabels=tickers,cmap='binary' ,ax=axes[0],cbar=False)
axes[0].set_title("2019/01/16 - 2020/01/15 ", size=14)

sns.heatmap(Causal_Matrix[77],xticklabels=tickers, yticklabels=tickers, cmap='binary',ax=axes[1],cbar=False)
axes[1].set_title("2019/04/07 - 2020/04/16 ",size=14)


plt.savefig('Causality_heatmap_USA.pdf')
plt.show()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# The dynamics of the average causality 

date_MeanCausality = list(zip(Date,Mean_causality))  
df_ave_Causality = pd.DataFrame(date_MeanCausality, columns=['date','Causality'])  

df_ave_Causality.to_csv('Mean_Causality_USA.csv')

df_ave_Causality=df_ave_Causality.set_index('date')
df_ave_Causality.plot(figsize=(14,6),marker='o')


