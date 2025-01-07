from binance.client import Client
import datetime
import keys

# Your Binance API keys (replace with your own)
api_key = keys.api_key
api_secret = keys.api_secret

# Initialize the Binance client
client = Client(api_key, api_secret)

def get_price_changes(pair: str, change_threshold: float = 4) -> int:
    # Get the historical daily candlestick data for the pair (candles for the last 365 days)
    candles = client.get_historical_klines(pair, Client.KLINE_INTERVAL_1DAY, "1 year ago UTC")

    # Initialize a counter for the number of days with > 4% price change
    days_with_large_change = 0
    
    for candle in candles:
        # Get the open and close prices (candle[1] is open, candle[4] is close)
        open_price = float(candle[1])
        close_price = float(candle[4])
        
        # Calculate the percentage change
        price_change_percent = ((close_price - open_price) / open_price) * 100
        
        # Check if the price change is greater than 4% in either direction
        if abs(price_change_percent) > change_threshold:
            days_with_large_change += 1
    
    return days_with_large_change

# Example usage
pair = str(input("Enter the pair you want to check: "))
change_threshold = float(input("Enter the price change threshold in %: "))
days = get_price_changes(pair, change_threshold)
print(f"The number of days in the year when the price of {pair} changed by more than 4% is: {days}")
