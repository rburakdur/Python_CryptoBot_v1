import requests
import datetime


def telegram_bot_sendtext(symbol="NONE", interval="NONE",  current="NONE", resistance="NONE", support="NONE", stop="NONE", status="NONE"):

    current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    bot_message = f"{symbol}\t\t{interval}\n{status}\nNow : {current}\nResistance : {resistance}\nSupport : {support}\nStop : {stop}\nTime : {current_time}"
    bot_token = "1549960256:AAHtjmQztPYKSW_BwVxXiPpf7Dnca8w4LgY"
    bot_chatID = "-1001466370685"
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


# telegram_bot_sendtext("xd")
