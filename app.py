from flask import Flask, render_template
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
    data = geter()
    return render_template("index.html", data=data, response=geter())


app.run(debug=True)
