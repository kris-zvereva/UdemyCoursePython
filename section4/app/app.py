from flask import Flask

app = Flask(__name__)  # identify the app uniquely


@app.route('/')  # endpoint http://mysite.com/
def home():
    return{'message': 'Hello, world!'}


if __name__ == '__main__':
    app.run()
