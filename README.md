# Collective behavior of stock prices in the time of crisis as a response to the external stimulus
In this repository, I look for the interaction between stock prices of 27 big US companies using correlation and Granger causality matrices. I found that the pair-wise Granger causality interaction between prices in the times of crisis is increasing, and conclude that would be the consequence of simultaneous response of the markets to the outside events or external stimulus that is considered as a common driver to all the stocks, not a result of real causal predictability between the prices themselves. I modelled, the observed patterns in the price of by adding a multiplicative exogenous term as the representative for external factors to the geometric Brownian motion model for stock prices. Altogether, I can detect and model the effects of the Great Recession as a consequence of the mortgage crisis in 2007/2008 as well as the impacts of the Covid out-break in early 2020.

# Granger causality test between stock prices of companies

Granger causality (GC) is a statistical method, introduced for the first time in the field of econometrics [[1,2]](#1), to study the causal interaction between two or multiple time series. E.g. in the case of two time series, GC quantifies whether one series helps forecasting the other. The method is based on two main premises, namely
 (i) cause happens before its effect and (ii) observing the cause can improve the predictability of its effect. 
Consider two time series, ${x_{t}}$ and ${y_{t}}$, recorded simulataneously. The series ${x_{t}}$ Granger causes ${y_{t}}$ if ${x_{t}}$ contains some information which can be used for improving the forecast accuracy of ${y_{t}}$, alongside the past values of ${y_{t}}$ itself. Granger causality is thus a measure of predictability, allowing the evaluation of the usefulness of one time-series in forecasting another. The linear Granger causality from series $x_t$ to $y_t$ could be formulated mathematically using vector auto-regressive model (VAR) as follows:
$$y_t = \alpha_{0} + \sum_{l=1}^{l=\tau^{'}} \alpha_{l} y_{t-l} + \sum_{l=1}^{l=\tau} \beta_{l} x_{t-l} + \epsilon_t.$$
where $\tau^{'}$ and $\tau$ are the maximum lag times, and $\epsilon_t$ is the residual of the forecast.
The maximum lags have to be chosen such that all past observations make a statistically significant contribution to the forecast.
In the above bi-variate causal model ${x_{t}}$ Granger causes ${y_{t}}$ if the coefficients $\beta_{l}$ are different from zero and statistically significant. The latter can be tested using an F-test with the null hypothesis that all the $\beta_{l}$ coefficients are zero. 

I applied this type of bivariate VAR model in a windowed framework, creating an asymmetric matrix of binary results: granger causal or not. Furthermore, note that Granger causality can only be applied for the stationary time series. Therefore, before applying it, one has to make sure of stationary of the time series under study, in this case the log-return of the time series of prices. 

I used the Granger causality test for the pairwise interaction between stock prices of companies in Dow Jones Industrial Average (DJIA). Some companies from these two indices are excluded, because of unavailability of data during the time period of study. So altogether I analysed 27 big companies in the USA. Data are collected from Yahoo finance and contain the daily stock prices of the companies since the beginning of 2000. The time series of the log-returns of the prices were divided into moving windows with the length of 252 days (number of working days in a year) and the step size of 63 days. Each window is marked with the date of the middle of the window.

# Geometrical Brownian Motion

Geometrical Brownian Motion or in short GBM model is considered as a standard model for stock price dynamics [[3]](#1). 
The model assumes that the logarithm of random variables ${X}$ follows a Brownian motion and can be expressed by the following stochastic differential equation [[4,5]](#1),

$$ dX(t)=\mu X(t)dt+\sigma X(t)dW(t). $$

When modelling stock prices by GBM, $X(t)$ in above equation is considered as price at time $t$, $\mu$ is the drift term or the mean of the price and $\sigma$ is the volatility of the market. $dW$ is the increment of Wiener process which is white Gaussian noise. Using Ito's lemma, the price at time $t$ by solving above equation is

$$ X(t)=X_{0} e^{(\mu-\frac{\sigma^{2}}{2})t+\sigma W(t)},$$

$X_{0}$ is the price at time $t=0$. 

# Modelling the stock prices by adding an extra term to the GBM

In order to model the observed patterns in the dynamics of causality interaction between the stock prices, I added an extra exogenous term to the log-return of prices.  
For that, consider an additional term in above equation called $H(t)$ which represents any external driver that can affect the market price in different degrees. I rewrite the above equation by adding an extra term related to the external driver,

$$ dX(t)=\mu X(t)dt+\beta h(t) X(t) dt +\sigma X(t)dW(t), $$

where $h(t)=\frac{dH(t)}{dt}$ and the  coefficient $\beta$ represents the rate of influence which is a number between 0 and 1. The solution of the above equation is

$$ X(t)=X_{0} e^{(\mu-\frac{\sigma^{2}}{2})t+\sigma W(t)+\beta H(t)}.$$

Postulating the right function for the external influence is impossible, since there are different factors that affect market movements;  effects can be short or long, weak or strong, from a tweet of some influential person over a hurricane to a terrorism attack and even bigger effects like mortgages crisis and pandemic. The fact is, we never know what is going to happen, there is an unpredictable factor with a huge influence on the market's price that can never be predicted, so that this model cannot be used for forecasting. However, retrospectively, we can construct $h(t)$ from the ensemble of observed stock price time series. 
If we assume that each single price sequence is generated by above equation, with individual $\mu$, $\sigma$, $\beta$, and we devide by $X(t)$, then this equation becomes an equation for the log-returns. Averaging over all stocks, 
the common driver $h(t)$ will survive, while the increments of the Wiener process $dW$ will (almost) cancel out since the ensemble mean of $dW$ equalts 0. 
What is left is the average over the unknown drift terms $\mu$, which we can remove by requiring zero mean for $h(t)$. Hence, the way to identify $h(t)$ is to calculate the ensemble average of the log-returns of the different stocks. In order to make $h(t)$ smoother, I performed an additional moving-window average.





## References
<a id="1">[1]</a> 
Granger, Clive WJ. (1969). 
Investigating causal relations by econometric models and cross-spectral methods. 
Econometrica: journal of the Econometric Society, 37, 424-438.

<b id="2">[2]</b> 
Granger, Clive WJ. (1980). 
Testing for causality: A personal viewpoint. 
Journal of Economic Dynamics and control, 2, 329-352.

<c id="3">[3]</c> 
Mantegna, Rosario N and Stanley, H Eugene. (1999). 
Introduction to econophysics: correlations and complexity in finance. 
Cambridge university press.

<d id="4">[4]</d> 
Fouque, Jean-Pierre and Papanicolaou, George and Sircar, K Ronnie. (2000). 
Derivatives in financial markets with stochastic volatility. 
Cambridge university press.

<e id="5">[5]</e> 
McCauley, Joseph L. (2013). 
Stochastic calculus and differential equations for physics and finance. 
Cambridge university press.





