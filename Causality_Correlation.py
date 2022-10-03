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
from sklearn.metrics import r2_score


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




