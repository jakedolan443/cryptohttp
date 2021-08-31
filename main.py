import flask
import sys
from server import Server


help_menu = "USAGE: ./cryptohttp <ARGS>\n  --host <HOST>\t\thost to bind to, default 0.0.0.0\n  --port <PORT>\t\tport to bind to, default 8080\n  --refresh <RATE>\thow often to refresh API data, in seconds, default 3600\n  --detach\t\trun cryptohttp in the background."

host = "0.0.0.0"
port = 8080
refresh_rate = 3600

for entry in sys.argv:
    try:
        if entry == "--host":
            host = sys.argv[sys.argv.index(entry)+1]
        elif entry == "--port":
            port = int(sys.argv[sys.argv.index(entry)+1])
        elif entry == "--refresh":
            refresh_rate = int(sys.argv[sys.argv.index(entry)+1])
        elif entry == "--help":
            print(help_menu)
            exit()
    except Exception:
        print(help_menu)
        exit()

app = flask.Flask(__name__, static_url_path='')
@app.route("/")
def serve():
    data = server.get_data()
    return flask.render_template("index.html", data=data)


if __name__ == "__main__":
    server = Server(refresh_rate)
    app.run(host, port=port)
    
    
