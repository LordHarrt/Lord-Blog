from flask import Flask
from config import DevConfig


app = Flask(__name__)


# Get the config from object of Devconfig
app.config.from_object(DevConfig)


# View
@app.route("/")
def home():
    return "<h1>Hello Wuyanzu!"


if __name__ == '__main__':
    # Entry the application
    app.run()