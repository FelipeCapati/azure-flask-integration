from flask import Flask
application = Flask(__name__)


@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello Andre!! Isso foi Atualizado com CI/CD</h1>"


if __name__ == "__main__":
    # Add comment to init build
    application.run(host='0.0.0.0')