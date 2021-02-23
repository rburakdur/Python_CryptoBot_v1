from flask import Flask, render_template, request
import txt_db
import bot_start
import threading


app = Flask(__name__)


def bot():
    bot_start.main()


t = threading.Thread(target=bot)
t.daemon = True
t.start()


def geter():
    datas = txt_db.oku()
    revers = datas[::-1]
    return revers


@app.route('/', methods=["GET"])
def first():
    if request.method == 'GET':
        return "burdaydık"
    else:
        data = geter()
        return render_template("index.html", data=data)


@app.route('/datas')
def veri():
    with open("db.txt", "r") as f:
        return render_template("datas.html", text=f.read())


@app.route('/cron', methods=['GET'])
def cron():
    if request.method == 'GET':
        return "burdaydık"


if __name__ == '__main__':
    app.run(debug=False)
