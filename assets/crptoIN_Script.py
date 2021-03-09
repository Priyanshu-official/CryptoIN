import requests
import time

# WE ARE USING COINBASE API TO GET INFO OF CRYPTOCURRENCY

token = "1563898178:AAFOhpfwUJTUw3PVN-H2pfMmXu46z0F-1Pc"
chat_id = "911573314"

threshold = 2580770  # just the price of 1 bitcoin in INR at the time of writing this script

# it will send a request to coinbase API every 5 minutes
time_interval = 5*60

def send_message(chat_id, msg):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"

    # send the msg
    requests.get(url)

def crypto_price():
    # Available cryptocurrencies are 'BTC', 'ETH', 'ETC', 'BCH', 'LTC', 'ZEC', 'ZRX'
    # More info at documentation site of coinbase API. 

    cryptocurrency = "BTC"
    response_obj = requests.get(
        'https://api.coinbase.com/v2/exchange-rates?currency='+cryptocurrency)

    try:
        exchange_dict = response_obj.json()["data"]["rates"]
    except KeyError:
        return None

    # get current_price for cryptocurrency using exhange_rates function
    current_price = exchange_dict["INR"]

    return float(current_price)

def main():
    # infinite loop
    while True:
        price = crypto_price()
        # if the price falls below threshold, send an immediate msg
        if price < threshold:
            send_message(chat_id=chat_id, msg=f'Price Drop Alert: {price}')

        #waits 10 minutes before sending a message
        time.sleep(time_interval)
        price = crypto_price()
        send_message(chat_id=chat_id, msg=f'BTC Price Drop Alert: {price}')


if __name__ == '__main__':
    print("running the script")
    main()
