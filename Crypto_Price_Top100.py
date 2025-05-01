import requests

# Récupère le top 100 des cryptos selon leur market cap
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

# Affiche les prix
def display_crypto_prices(crypto_list):
    print("Price of Top 100 Cryptos by capitalisation:")
    print("-" * 40)
    for crypto in crypto_list:
        name = crypto['name']
        symbol = crypto['symbol'].upper()
        price = crypto['current_price']
        print(f"{name} ({symbol}): ${price:,.2f}")

# Exécution
cryptos = get_top_cryptos()
display_crypto_prices(cryptos)
