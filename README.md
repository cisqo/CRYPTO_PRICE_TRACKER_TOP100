# 🪙 Crypto Price Tracker

A simple Python script that displays the **Top 100 cryptocurrencies** (by market cap) with their **real-time prices in USD**, using the free [CoinGecko API](https://www.coingecko.com).

---

## 🚀 Features

- 🔄 Dynamically fetches the top 100 most valuable cryptocurrencies
- 💵 Displays live prices in USD
- 📦 Powered by the public CoinGecko API (no key needed)
- 🔧 Easy to modify or extend

---

## 🧑‍💻 Code Preview

```python
import requests

def get_top_cryptos(limit=100):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    return response.json()

def display_crypto_prices(crypto_list):
    print("Top 100 Cryptos by Market Cap:")
    print("-" * 40)
    for crypto in crypto_list:
        name = crypto['name']
        symbol = crypto['symbol'].upper()
        price = crypto['current_price']
        print(f"{name} ({symbol}): ${price:,.2f}")

cryptos = get_top_cryptos()
display_crypto_prices(cryptos)
