from flask import Flask, jsonify

app = Flask(__name__)  # identify the app uniquely


@app.route('/')  # endpoint http://mysite.com/
def home():
    return jsonify({'message': 'Hello, world!'})


if __name__ == '__main__':
    app.run()
