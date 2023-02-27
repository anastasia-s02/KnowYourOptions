import streamlit as st
import os
from math import log, sqrt, exp
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def d1(stock_price, strike_price, risk_free_rate, volatility, time_until_maturity):
    """
    Calculates intermediate term d1 for Black-Scholes model.
    """

    return (
        log(stock_price / strike_price)
        + (risk_free_rate + volatility**2 / 2) * time_until_maturity
    ) / (volatility * sqrt(time_until_maturity))


def d2(stock_price, strike_price, risk_free_rate, volatility, time_until_maturity):
    """
    Calculates intermediate term d2 for Black-Scholes model.
    """

    return (
        log(stock_price / strike_price)
        + (risk_free_rate - volatility**2 / 2) * time_until_maturity
    ) / (volatility * sqrt(time_until_maturity))


def calculate_call_price(
    stock_price, strike_price, risk_free_rate, volatility, time_until_maturity
):
    """
    Calculates option call price according to  Black-Scholes model.
    """

    return stock_price * norm.cdf(
        d1(stock_price, strike_price, risk_free_rate, volatility, time_until_maturity)
    ) - strike_price * exp(-risk_free_rate * time_until_maturity) * norm.cdf(
        d2(stock_price, strike_price, risk_free_rate, volatility, time_until_maturity)
    )


def calculate_put_price(
    stock_price, strike_price, risk_free_rate, volatility, time_until_maturity
):
    """
    Calculates option put price according to  Black-Scholes model.
    """

    return strike_price * exp(-risk_free_rate * time_until_maturity) * norm.cdf(
        -d2(stock_price, strike_price, risk_free_rate, volatility, time_until_maturity)
    ) - stock_price * norm.cdf(
        -d1(stock_price, strike_price, risk_free_rate, volatility, time_until_maturity)
    )


def plot_black_scholes_call(
    stock_price, strike_price, risk_free_rate, volatility, time_until_maturity
):
    """
    Plots a graph of the call price according to  Black-Scholes model.
    """

    figure, axes = plt.subplots()
    axes.set_xlabel("Stock Price")
    axes.set_ylabel("Call Option Price")
    axes.set_title("Black-Scholes Formula for Call Option")

    # Create an array of stock prices ranging from 0.5*stock_price to 1.5*stock_price
    stock_price_values = np.linspace(0.5 * stock_price, 1.5 * stock_price, 100)

    # Calculate the corresponding call option prices using the Black-Scholes formula
    call_prices = [
        calculate_call_price(
            stock_price, strike_price, risk_free_rate, volatility, time_until_maturity
        )
        for stock_price in stock_price_values
    ]

    # Plot the call option prices as a function of stock price
    axes.plot(stock_price_values, call_prices)

    return figure


def plot_black_scholes_put(
    stock_price, strike_price, risk_free_rate, volatility, time_until_maturity
):
    """
    Plots a graph of the put price according to  Black-Scholes model.
    """

    figure, axes = plt.subplots()
    axes.set_xlabel("Stock Price")
    axes.set_ylabel("Put Option Price")
    axes.set_title("Black-Scholes Formula for Put Option")

    # Create an array of stock prices ranging from 0.5*stock_price to 1.5*stock_price
    stock_price_values = np.linspace(0.5 * stock_price, 1.5 * stock_price, 100)

    # Calculate the corresponding put option prices using the Black-Scholes formula
    put_prices = [
        calculate_put_price(
            stock_price, strike_price, risk_free_rate, volatility, time_until_maturity
        )
        for stock_price in stock_price_values
    ]

    # Plot the put option prices as a function of stock price
    axes.plot(stock_price_values, put_prices)

    return figure


def create_nav_menu():
    """
    Creates navigation menu.
    """

    nav_menu = ["Home", "What are options?", "Black-Scholes Visualization"]
    nav_choice = st.sidebar.radio("Select a page:", nav_menu)
    return nav_choice


if __name__ == "__main__":
    # Set page title and creates navigation menu
    st.set_page_config(page_title="OPTimal", page_icon=":chart_with_upwards_trend:")
    nav_choice = create_nav_menu()

    # Define the content for Home page
    if nav_choice == "Home":
        st.markdown('<div class="bg-image"></div>', unsafe_allow_html=True)

        # Add header and subheader
        st.header("OPTimal!")
        st.subheader("Learn how to trade options and supercharge your portfolio")
        st.image(os.path.join("", "cover.jpg"))
    # Define the content for page with Black-Scholes visualization
    elif nav_choice == "Black-Scholes Visualization":
        # Set page header and description
        st.title("Black-Scholes Formula Visualization")
        st.write(
            "This app lets you see how the Black-Scholes formula "
            + "can be used to price European call and put options on a stock."
        )

        # Set sidebar and sliders
        st.sidebar.title("Input Parameters")
        stock_price = st.sidebar.slider(
            "Current stock price (S), $", min_value=1, max_value=1000, value=100
        )
        strike_price = st.sidebar.slider(
            "Option striking price (K), $", min_value=1, max_value=1000, value=100
        )
        risk_free_rate = st.sidebar.slider(
            "Risk-free interest rate (r)",
            min_value=0.0,
            max_value=1.0,
            value=0.05,
            step=0.01,
        )
        volatility = st.sidebar.slider(
            "Volatility (sigma)", min_value=0.0, max_value=1.0, value=0.2, step=0.01
        )
        time_until_maturity = st.sidebar.slider(
            "Time to expiration (T)",
            min_value=0.01,
            max_value=1.0,
            value=0.5,
            step=0.01,
        )

        # Plot a graph for call price
        call_price = calculate_call_price(
            stock_price, strike_price, risk_free_rate, volatility, time_until_maturity
        )
        st.write(
            f"**Given the input parameters, the call option price is:** `{call_price:.2f}`"
        )
        call_figure = plot_black_scholes_call(
            stock_price, strike_price, risk_free_rate, volatility, time_until_maturity
        )
        st.pyplot(call_figure, dpi=150)

        # Description of call price plot
        st.write(
            "The plot above shows how the price of the call option changes with "
            + "the price of the stock. You can see that as the stock price goes up, "
            + "the value of the call option also goes up. This is because the holder "
            + "of the call option has the right to buy the stock at a lower price than "
            + "the market price, and thus stands to profit from the increase in the stock price."
        )

        # Plot a graph for put price
        put_price = calculate_put_price(
            stock_price, strike_price, risk_free_rate, volatility, time_until_maturity
        )
        st.write(
            f"**Given the input parameters, the put option price is:** `{put_price:.2f}`"
        )
        put_figure = plot_black_scholes_put(
            stock_price, strike_price, risk_free_rate, volatility, time_until_maturity
        )
        st.pyplot(put_figure, dpi=150)

        # Description of put price plot
        st.write(
            "The plot above shows how the price of the put option changes with "
            + "the price of the stock. You can see that as the stock price goes up, "
            + "the value of the put option also goes down. This is because the holder "
            + "of the put option has the right to sell the stock at a higher price than "
            + "the market price, and thus stands to profit from the decrease in the stock price."
        )
    # Define the content for page with short description of what options are
    elif nav_choice == "What are options?":
        # Add text
        st.header("What are options?")
        st.image(os.path.join("", "graph.png"))
        st.write(
            "Options are contracts that give the holder the right, but not the obligation, "
            + "to buy or sell an underlying asset at a predetermined price, within a specified "
            + "time period. The underlying asset can be a stock, an index, a commodity, or a currency."
        )
        st.write(
            "There are two types of options: calls and puts. A call option gives the holder the right "
            + "to buy an underlying asset at a predetermined price, while a put option gives the holder "
            + "the right to sell an underlying asset at a predetermined price."
        )
        st.write(
            "The price of an option is determined by several factors, including the current price of "
            + "the underlying asset, the strike price, the time to expiration, and the volatility of "
            + "the underlying asset."
        )
        st.write(
            "Suppose you want to buy a call option on a stock that is currently trading at \$100. "
            + "The strike price of the option is \$110, and the option expires in one month. "
            + "The premium (price) of the option is \$5. If you buy the option and the stock "
            + "price goes up to \$120 by the expiration date, you can exercise the option and "
            + "buy the stock at the strike price of \$110, making a profit of \$5 per share."
        )
