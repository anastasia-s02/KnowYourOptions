
# OPTimal #

### Do you know about option trading? If you are not familar, check out [this link](https://www.youtube.com/watch?v=joJ8mbwuYW8&ab_channel=SkyViewTrading!) ###

https://www.youtube.com/watch?v=joJ8mbwuYW8&ab_channel=SkyViewTrading

### What is a fair value of an option and why is it important to get the most accurate prediction? ###

![image](https://user-images.githubusercontent.com/63567363/219904458-54558b24-e88a-4765-a0fa-e1f4e74a113e.png)

This value is important to know because it can be used to ascertain whether an option is expensive or reasonably priced. Option traders use fair value as a reference, and profit by purchasing options for less than their fair value or selling them for more than their fair value.

### How does the Black-Scholes model work? ###

The Black Scholes model works by using a stock's volatility, current price, strike price, risk-free interest rate for a stable asset, and time to maturity to determine fair the price of a stock option.

### Assumptions ###

The original Black-Scholes model is based on a core assumption that the market consists of at least one risky asset (such as a stock) and one (essentially) risk-free asset, such as a money market fund, cash or a government bond. In addition, it assumes three properties of the two assets, and four of the market itself:

<ins>Assumptions about the assets in the market are:</ins>
* The rate of return on the risk-free asset is constant (thus effectively behaves as an interest rate).
* The instantaneous log return of the risky asset’s price is assumed to behave as an infinitesimal random walk with constant drift and volatility, more precisely, according to geometric Brownian motion.
* The risky asset does not pay a dividend.

<ins>Assumptions about the market itself are:</ins>
* There are no arbitrage (risk-free profit) opportunities.
* It is possible to borrow and lend any amount of cash at the same rate as the interest rate of the risk-free asset.
* It is possible to buy and sell any amount of the stock (including short selling).
* There are no transaction costs in the market (i.e. no commission for buying or selling securities or derivative instruments).




### How to Run the Program ###



After cloning git repository, run the following commands in the terminal:

```
pip install streamlit
```
```
streamlit run options.py
```
