import streamlit as st
from math import log, sqrt, exp
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

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

# Set page title and favicon
st.set_page_config(page_title="Options Trading 101", page_icon=":chart_with_upwards_trend:")

# Define a function to create the navigation menu
def create_nav_menu():
    nav_menu = ["Home","Black-Scholes",  "Basic Concepts", "Examples", "Resources"]
    nav_choice = st.sidebar.radio("Select a page:", nav_menu)
    return nav_choice

# Create the navigation menu
nav_choice = create_nav_menu()

# Define the content for each page
if nav_choice == "Home":
    st.markdown('<div class="bg-image"></div>', unsafe_allow_html=True)

    # Add header and subheader
    st.header("Welcome to Options Trading 101")
    st.subheader("Learn how to trade options and supercharge your portfolio")

    # Add call-to-action button
    if st.button("Get Started"):
        nav_choice = "Basic Concepts"

elif nav_choice == "Black-Scholes":
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


elif nav_choice == "Basic Concepts":
    # Add text
    st.header("Basic Concepts")

    st.write("Options are contracts that give the holder the right, but not the obligation, to buy or sell an underlying asset at a predetermined price, within a specified time period. The underlying asset can be a stock, an index, a commodity, or a currency.")

    st.write("There are two types of options: calls and puts. A call option gives the holder the right to buy an underlying asset at a predetermined price, while a put option gives the holder the right to sell an underlying asset at a predetermined price.")

    st.write("The price of an option is determined by several factors, including the current price of the underlying asset, the strike price, the time to expiration, and the volatility of the underlying asset.")

    st.write("Suppose you want to buy a call option on a stock that is currently trading at \$100. The strike price of the option is \$110, and the option expires in one month. The premium (price) of the option is \$5. If you buy the option and the stock price goes up to \$120 by the expiration date, you can exercise the option and buy the stock at the strike price of \$110, making a profit of \$5 per share.")


elif nav_choice == "Examples":
    # Add text
    st.header("Examples")

    st.write("Here are some example trades you can make with options:")

    st.write("- Buy a call option if you think the price of an underlying asset will go up")
    st.write("- Buy a put option if you think the price of an underlying asset will go down")
    st.write("- Sell a call option if you think the price of an underlying asset will stay the same or go down")
