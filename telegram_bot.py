import requests
import datetime


current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

# SENDER


def telegram_bot_sendtext(bot_message):
    bot_token = "1549960256:AAHtjmQztPYKSW_BwVxXiPpf7Dnca8w4LgY"
    bot_chatID = "-1001466370685"
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def buy_message(tg):

    asd = ""
    for i in range(len(tg)):
        asd += (tg[i] + "\n" + "--------------------------\n")
    buy_message = f"{asd}\n{current_time}"
    telegram_bot_sendtext(buy_message)


def profit_message(prf):
    bot_message = f"{prf}\n" + \
        "--------------------------\n" + f"{current_time}"
    telegram_bot_sendtext(bot_message)
