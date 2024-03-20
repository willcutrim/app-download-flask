from apps.urls import add_routes
from flask import Flask

app = Flask(__name__)


add_routes(app)


if __name__ == '__main__':
    app.run(debug=True)