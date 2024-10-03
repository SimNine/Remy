from flask import Flask

def main():
    app = Flask(__name__)


    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True,
    )

main()