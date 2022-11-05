import requests

token = "5531466079:AAG3-eD9qonfG82gP0qoz5wJqN-2S_GvPK4"

chat_id = "-1001844051429"

parse_mode = "HTML"

url = f"https://api.telegram.org/bot{token}/sendMessage"

payload = {
    "chat_id": chat_id,
    "text": "Required",
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




# import requests

# url = "https://api.telegram.org/bot5531466079:AAG3-eD9qonfG82gP0qoz5wJqN-2S_GvPK4/getUpdates"

# print(url)
# payload = {
#     "offset": None,
#     "limit": None,
#     "timeout": None
# }
# headers = {
#     "accept": "application/json",
#     "content-type": "application/json"
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.text)