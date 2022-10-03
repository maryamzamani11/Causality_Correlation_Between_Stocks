

import numpy as np
import matplotlib.pyplot as plt

    
def Generate_gbm(n,X0,Mu,sigma):
    Noise = np.array(np.random.normal(0,1,n))
    Wt = np.cumsum(Noise)
    t = np.arange(n)
    step = X0*np.exp((Mu-(sigma**2)/2)*t)*np.exp(sigma*Wt)
    return step

# n: length of the time series 
# X0: initial close price of stocks at time t=0 
# Mu: mean of the log-return of stocks
# sigma: std of the log-return
plt.plot(Generate_gbm(1000,66.81,0.00013,0.014))
