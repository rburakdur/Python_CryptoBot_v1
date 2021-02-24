import json
import telegram_bot as tbot
filename = 'db.txt'


def New_data(symbol="NONE", interval="NONE", resistance="NONE", support="NONE", stop="NONE", ema14="NONE", ema_stop="NONE"):

    coin_data = {f"{symbol}": [{
        f"{interval}": [{
            "resistance": f"{resistance}",
            "support": f"{support}",
            "stop": f"{stop}",
            "ema14": f"{ema14}",
            "ema_stop": f"{ema_stop}"
        }]
    }]
    }

    try:
        a1 = Get_data()
        a2 = a1[symbol][0]
        a2.update(coin_data[symbol][0])
        Write_data(a1)
    except:
        r = Get_data()
        r.update(coin_data)
        Write_data(r)


def Write_data(newData):
    with open(filename, "w") as f:
        f.write(json.dumps(newData, indent=4))
        f.close()


def Get_data():
    with open(filename, "r") as js:
        opened = json.loads(js.read())
        js.close()
        return opened
# to web


def oku():
    with open("webList.txt", "r") as js:
        asd = json.loads(js.read())
        return asd


def yaz(ls):
    with open("webList.txt", "w") as js:
        js.write(json.dumps(ls, indent=4))
        js.close()


def update(cs):
    ls = list(cs)
    a = oku()
    varmi = False
    for i in range(len(a)):
        if (a[i][0] == ls[0]) and (a[i][1] == ls[1]) and (a[i][2] == ls[2]):

            a.pop(i)
            a.append(ls)
            yaz(a)
            varmi = True

            print("var bundan")
    if not varmi:
        a.append(ls)
        yaz(a)
        print("yazdık")


p = "ANKRUSDT", "1h", 456, 456, 789, 741, 123456789, "Al"
#w = "RENUSDT", "15m", 456, 123, 789, 456, 456, "Sat"


# if (a[i][0] == ls[0]) and (a[i][1] == ls[1]) and (a[i][2]] == ls[2]):
#           a.remove(i)
#            a.insert(i, ls)
