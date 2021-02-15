import json
import telegram_bot as tbot
filename = 'db.txt'


def New_data(symbol="NONE", interval="NONE", resistance="NONE", support="NONE", stop="NONE"):
    coin_data = {f"{symbol}"f"{interval}": [{
        "resistance": f"{resistance}",
        "support": f"{support}",
        "stop": f"{stop}"}
    ]

    }

    getted_data = Get_data()
    getted_data.update(coin_data)
    Write_data(getted_data)


def Write_data(newData):
    with open(filename, "w") as f:
        f.write(json.dumps(newData, indent=4))


def Get_data():
    with open(filename, "r") as js:
        opened = json.loads(js.read())
        return opened


#xd = Get_data().keys()
# print(xd)
# csssss = {"BTCUSDT15m": [{
#    "resistance": "150000",
#    "support": "120546",
#    "stop": "1"}
# ]}


#
#a1 = dict(Get_data())
# a1.update(csssss)
# print(a1)
# Write_data(a1)
