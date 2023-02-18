import streamlit as st
import numpy as np
from scipy.stats import norm
from math import log, sqrt, exp
import matplotlib.pyplot as plt

def d1(S, K, r, sigma, T):
    return (log(S/K) + (r + sigma**2/2)*T) / (sigma * sqrt(T))

def d2(S, K, r, sigma, T):
    return (log(S/K) + (r - sigma**2/2)*T) / (sigma * sqrt(T))

def calculate_call_price(S, K, r, sigma, T):
    return S * norm.cdf(d1(S, K, r, sigma, T)) - K * exp(-r*T) * norm.cdf(d2(S, K, r, sigma, T))

def plot_black_scholes(S, K, r, sigma, T):
    fig, ax = plt.subplots()
    ax.set_xlabel('Stock Price')
    ax.set_ylabel('Call Option Price')
    ax.set_title('Black-Scholes Formula')

    # Create an array of stock prices ranging from 0.5*S to 1.5*S
    S_values = np.linspace(0.5*S, 1.5*S, 100)

    # Calculate the corresponding call option prices using the Black-Scholes formula
    call_prices = [calculate_call_price(S, K, r, sigma, T) for S in S_values]

    # Plot the call option prices as a function of stock price
    ax.plot(S_values, call_prices)

    return fig

st.set_page_config(page_title='Options Trading', page_icon=':chart_with_upwards_trend:')

st.sidebar.title('Options Trading')

menu = ['Black-Scholes Formula', 'What are options?']
choice = st.sidebar.selectbox('Select an option', menu)

if choice == 'Black-Scholes Formula':
    st.title('Black-Scholes Formula Demo')
    st.write('This app lets you see how the Black-Scholes formula can be used to price a European call option on a stock.')

    st.sidebar.title('Input Parameters')
    S = st.sidebar.slider('Stock price (S)', min_value=1, max_value=1000, value=100)
    K = st.sidebar.slider('Strike price (K)', min_value=1, max_value=1000, value=100)
    r = st.sidebar.slider('Risk-free rate (r)', min_value=0.0, max_value=1.0, value=0.05, step=0.01)
    sigma = st.sidebar.slider('Volatility (sigma)', min_value=0.0, max_value=1.0, value=0.2, step=0.01)
    T = st.sidebar.slider('Time to expiration (T)', min_value=0.01, max_value=1.0, value=0.5, step=0.01)

    call_price = calculate_call_price(S, K, r, sigma, T)

    st.write(f'**Given the input parameters, the call option price is:** `{call_price:.2f}`')

    fig = plot_black_scholes(S, K, r, sigma, T)
    st.pyplot(fig, dpi=150)
    st.write('The plot above shows how the price of the call option changes with the price of the stock. You can see that as the stock price goes up, the value of the call option also goes up. This is because the holder of the call option has the right to buy the stock at a lower price than the market price, and')
