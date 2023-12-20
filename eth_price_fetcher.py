import requests
import csv
from datetime import datetime

def fetch_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data["ethereum"]["usd"]
    return price

def save_price_to_csv(price):
    with open("eth_prices.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), price])

if __name__ == "__main__":
    eth_price = fetch_eth_price()
    save_price_to_csv(eth_price)
    print(f"✅ ETH price logged: ${eth_price}")
