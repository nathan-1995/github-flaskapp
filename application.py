from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello_wordl():
    return "Test v1"
