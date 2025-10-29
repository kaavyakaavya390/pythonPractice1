import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("command line arguments missing")
    
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("command line argument is not a number")
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=17f0d5ffd7861a63797581dd14725ae268d3615e21843fd946d4e30d63e45bf0"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price_usd = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error: Could not retrieve Bitcoin price")
    except (KeyError, ValueError):
        sys.exit("Error: Invalid response from API")
    total_cost = n * price_usd
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
