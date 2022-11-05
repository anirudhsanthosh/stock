import yfinance as yf
import pandas as pd 
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import requests


def send_stock_snapshot(file,start_date,end_date,interval):
    
    index = pd.read_csv(file, index_col=False)

    nifty_next_50 = index["SYMBOL \n"][1:]

    returns = {}

    for symbol in nifty_next_50:

        ticker = symbol+".NS"

        print(symbol)

        price = yf.download(ticker, start= start_date, end= end_date)

        # price.drop(["Adj Close", "Volume"], axis=1, inplace=True)

        month_open = price.iloc[0]["Open"]

        # month_close = price.iloc[-1]["Close"]
        month_close = price.iloc[-1]["Adj Close"]

        returns[symbol] = [(month_close / month_open) - 1, month_open, month_close]

    returns = {k: v for k, v in sorted(returns.items(), key=lambda item: item[1][0])}

    top_five = list(returns.items())[-5:]
    top_five.reverse()

    current_index = ' '.join(file.split('.')[0].split('-'))

    print("current_index",current_index)

    message = f"""<b>{current_index.upper()}</b>\n\n<b>Interval:</b>   <i>{interval} days</i>\n<b>Start Date:</b>    <i>{start_date}</i>\n<b>End Date:</b>   <i>{end_date}</i>\n"""

    rank = 1;
    for k, v in top_five:
        message += f"""
<b>{rank}. <code>{k}</code></b>
profit: <i>{ round( v[0],2)}%</i>
open:   <i>₹{ round( v[1] ,2) }</i>
close:  <i>₹{ round( v[2] ,2) }</i>\n"""
        rank +=1



    token = "5531466079:AAG3-eD9qonfG82gP0qoz5wJqN-2S_GvPK4"

    chat_id = "-1001844051429"

    parse_mode = "HTML"

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": parse_mode,
        "disable_web_page_preview": False,
        "disable_notification": False,
        "reply_to_message_id": 0
    }

    headers = {
        "accept": "application/json",
        "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)


#configs
interval = 30

categories = ["nifty-50.csv","nifty-next-50.csv"]

today = date.today()

tomarrow = today + datetime.timedelta(days=1)

last_month = today - datetime.timedelta(days=interval)

end_date = tomarrow.strftime("%Y-%m-%d")

start_date = last_month.strftime("%Y-%m-%d")

print("start_date", start_date)
print("end_date", end_date)

for category in categories:

    print(category)
    send_stock_snapshot(category,start_date,end_date,interval)