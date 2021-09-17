import os
import sys

import flask

from server import Server

help_menu = "USAGE: ./cryptohttp <ARGS>\n  --host <HOST>\t\thost to bind to, default 0.0.0.0\n  --port <PORT>\t\tport to bind to, default 8080\n  --refresh <RATE>\thow often to refresh API data, in seconds, default 3600\n  --detach\t\trun cryptohttp in the background."

host = "0.0.0.0"
port = 8080
refresh_rate = 3600

for entry in sys.argv:
    try:
        if entry == "--host":
            host = sys.argv[sys.argv.index(entry) + 1]
        elif entry == "--port":
            port = int(sys.argv[sys.argv.index(entry) + 1])
        elif entry == "--refresh":
            refresh_rate = int(sys.argv[sys.argv.index(entry) + 1])
        elif entry == "--help":
            print(help_menu)
            exit()
    except Exception:
        print(help_menu)
        exit()

if os.getenv("HOST"):
    host = os.getenv("HOST")
if os.getenv("PORT"):
    port = int(os.getenv("PORT"))
if os.getenv("REFRESH"):
    refresh_rate = int(os.getenv("REFRESH"))

app = flask.Flask(__name__, static_url_path="")


@app.route("/")
def serve():
    data = server.get_data()
    return flask.render_template("index.html", data=data)

@app.route("/markets/<code>")
def market(code):
    coin_name = server.query_coin_name(code)
    if coin_name:
        data = server.get_coin_data(code)
        return flask.render_template("market.html", data=data)
    else:
        return flask.abort(404)

@app.route("/markets/<code>.json")
def market_graph(code):
    data = server.get_graph_data(code)
    return flask.jsonify(data)


if __name__ == "__main__":
    server = Server(refresh_rate)
    app.run(host, port=port)
