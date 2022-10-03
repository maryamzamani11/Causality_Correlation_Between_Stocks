from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from statsmodels.tsa.api import VAR
from statsmodels.tools.eval_measures import rmse, aic
import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests, adfuller


start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2022, 1, 24)

# Import 27 of big US companies

# APPLE
AAPL = data.DataReader("AAPL", 'yahoo', start, end)

# AMGEN
AMGN = data.DataReader("AMGN", 'yahoo', start, end)

# AMERICAN EXPRESS
AXP = data.DataReader("AXP", 'yahoo', start, end)

# BOEING
BA = data.DataReader("BA", 'yahoo', start, end)

# CATERPILLAR
CAT = data.DataReader("CAT", 'yahoo', start, end)

# CISCO
CSCO = data.DataReader("CSCo", 'yahoo', start, end)

# CHEVRON
CVX = data.DataReader("CVX", 'yahoo', start, end)

# DISNEY
DIS = data.DataReader("DIS", 'yahoo', start, end)

# GOLDMAN SACHS
GS = data.DataReader("GS", 'yahoo', start, end)

# HOME DEPOT
HD = data.DataReader("HD", 'yahoo', start, end)

# HONEY WELL
HON = data.DataReader("HON", 'yahoo', start, end)

# IBM
IBM = data.DataReader("IBM", 'yahoo', start, end)

# INTEL
INTC = data.DataReader("INTC", 'yahoo', start, end)

# JOHNSON JOHNSON
JNJ = data.DataReader("JNJ", 'yahoo', start, end)

# JP MORGAN CHASE
JPM = data.DataReader("JPM", 'yahoo', start, end)

# COCA COLA
KO = data.DataReader("KO", 'yahoo', start, end)

# MCDONALD
MCD = data.DataReader("MCD", 'yahoo', start, end)

# MERK CO
MRK = data.DataReader("MRK", 'yahoo', start, end)

# 3M
MMM = data.DataReader("MMM", 'yahoo', start, end)

# MSFT
MSFT = data.DataReader("MSFT", 'yahoo', start, end)

# NIKE
NKE = data.DataReader("NKE", 'yahoo', start, end)

# Protector Gamble 
PG = data.DataReader("PG", 'yahoo', start, end)

# TRAVELERS
TRV = data.DataReader("TRV", 'yahoo', start, end)

# UNITED HEALTH GR
UNH = data.DataReader("UNH", 'yahoo', start, end)

# Verizon Communi  
VZ = data.DataReader("VZ", 'yahoo', start, end)

# WALL GREEN BOOTS
WBA = data.DataReader("WBA", 'yahoo', start, end)

# WALMART
WMT = data.DataReader("WMT", 'yahoo', start, end)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
tickers = ['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CSCO', 'CVX','DIS','GS','HD','HON','IBM','INTC','JNJ','JPM','KO','MCD'
          ,'MRK','MMM','MSFT','NKE','PG','TRV','UNH','VZ','WBA','WMT']

Companies = [AAPL, AMGN, AXP, BA, CAT, CSCO, CVX, DIS, GS, HD, HON, IBM, INTC, JNJ, JPM, KO, MCD
          , MRK, MMM, MSFT, NKE, PG, TRV, UNH, VZ, WBA, WMT]

# Concatanate all the stocks into a single dataframe

Stocks = pd.concat(Companies,axis=1,keys=tickers)
Stocks.columns.names = ['Company Ticker','Stock Info']

# Make two dataframes with pct_Change and log_return of close price

PCT_df = pd.DataFrame()
LogReturn_df = pd.DataFrame()

for ticker in tickers:
    PCT_df[ticker] = Stocks[ticker]['Close'].pct_change()
    LogReturn_df[ticker] = np.log(Stocks[ticker]['Close'])-np.log(Stocks[ticker]['Close'].shift(1))
    
LogReturn_df.dropna(inplace=True)

# Look for the dynamics of the correlation between stocks by considering a moving window with the size of 252 days and the step size of 63 days

Max_T = LogReturn_df.shape[0]
N=int(Max_T / 63)

Correlation_array = {}
Date_end_moving_Window = []
Average_Corr = []

for i in range(N-1):
    Correlation_array[i]=LogReturn_df.iloc[i*63:252+i*63].corr()
    Date_end_moving_Window.append(LogReturn_df.iloc[i*63:252+i*63].index[126])
    Average_Corr.append(Correlation_array[i].mean().mean())

    
date_MeanCorr = list(zip(Date_end_moving_Window,Average_Corr))  
df_ave_Corr = pd.DataFrame(date_MeanCorr, columns=['date','Corr'])  
df_ave_Corr=df_ave_Corr.set_index('date')
df_ave_Corr.plot(figsize=(14,6))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# plot the heatmap of the correlation in two different time windows
fig, axes = plt.subplots(1, 2, figsize=(18, 6))
sns.heatmap(Correlation_array[76],xticklabels=tickers, yticklabels=tickers,ax=axes[0])
axes[0].set_title("2019/01/16 - 2020/01/15 ", size=14)

sns.heatmap(Correlation_array[77],xticklabels=tickers, yticklabels=tickers,ax=axes[1])
axes[1].set_title("2019/04/07 - 2020/04/16 ", size=14)

plt.savefig('Correlation_heatmap_USA.pdf')
plt.show()
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


