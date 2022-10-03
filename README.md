# Collective behavior of stock prices in the time of crisis as a response to the external stimulus
In this repository, I look for the interaction between stock prices of 27 big US companies using correlation and Granger causality matrices. I found that the pair-wise Granger causality interaction between prices in the times of crisis is increasing, and conclude that would be the consequence of simultaneous response of the markets to the outside events or external stimulus that is considered as a common driver to all the stocks, not a result of real causal predictability between the prices themselves. I modelled, the observed patterns in the price of by adding a multiplicative exogenous term as the representative for external factors to the geometric Brownian motion model for stock prices. Altogether, I can detect and model the effects of the Great Recession as a consequence of the mortgage crisis in 2007/2008 as well as the impacts of the Covid out-break in early 2020.

# Granger causality test between stock prices of companies

Granger causality (GC) is a statistical method, introduced for the first time in the field of econometrics [[1]](#1), to study the causal interaction between two or multiple time series. E.g. in the case of two time series, GC quantifies whether one series helps forecasting the other. The method is based on two main premises, namely
 (i) cause happens before its effect and (ii) observing the cause can improve the predictability of its effect. 
Consider two time series, ${x_{t}}$ and ${y_{t}}$, recorded simulataneously. The series ${x_{t}}$ Granger causes ${y_{t}}$ if ${x_{t}}$ contains some information which can be used for improving the forecast accuracy of ${y_{t}}$, alongside the past values of ${y_{t}}$ itself. Granger causality is thus a measure of predictability, allowing the evaluation of the usefulness of one time-series in forecasting another. The linear Granger causality from series $x_t$ to $y_t$ could be formulated mathematically using vector auto-regressive model (VAR) as follows:
$$y_t = \alpha_{0} + \sum_{l=1}^{l=\tau^{'}} \alpha_{l} y_{t-l} + \sum_{l=1}^{l=\tau} \beta_{l} x_{t-l} + \epsilon_t.$$
where $\tau^{'}$ and $\tau$ are the maximum lag times, and $\epsilon_t$ is the residual of the forecast.
The maximum lags have to be chosen such that all past observations make a statistically significant contribution to the forecast.
In the above bi-variate causal model ${x_{t}}$ Granger causes ${y_{t}}$ if the coefficients $\beta_{l}$ are different from zero and statistically significant. The latter can be tested using an F-test with the null hypothesis that all the $\beta_{l}$ coefficients are zero. 

I applied this type of bivariate VAR model in a windowed framework, creating an asymmetric matrix of binary results: granger causal or not. Furthermore, note that Granger causality can only be applied for the stationary time series. Therefore, before applying it one has to make sure of stationary of the time series under study, in this case the log-return of the time series of prices. 

I used the Granger causality test for the pairwise interaction between stock prices of companies in Dow Jones Industrial Average (DJIA). Some companies from these two indices are excluded, because of unavailability of data during the time period of study. So altogether I analysed 27 big companies in the USA. Data are collected from Yahoo finance and contain the daily stock prices of the companies since the beginning of 2000. The time series of the log-returns of the prices were divided into moving windows with the length of 252 days (number of working days in a year) and the step size of 63 days. Each window is marked with the date of the middle of the window.

## References
<a id="1">[1]</a> 
Dijkstra, E. W. (1968). 
Go to statement considered harmful. 
Communications of the ACM, 11(3), 147-148.
