import flask
from server import Server


app = flask.Flask(__name__, static_url_path='')
@app.route("/")
def serve():
    data = server.get_data()
    return flask.render_template("index.html", data=data)


if __name__ == "__main__":
    server = Server()
    app.run("0.0.0.0", port=8080)
    
    
