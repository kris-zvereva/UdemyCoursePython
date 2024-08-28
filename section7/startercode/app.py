import os

from flask import Flask, jsonify, request
from flask_restful import Api
from flask_jwt_extended import JWTManager, create_access_token
from jwt import DecodeError

from section7.startercode.models.user import UserModel
from section7.startercode.resources.item import Item, ItemList
from section7.startercode.resources.store import Store, StoreList
from section7.startercode.resources.user import UserRegister

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


jwt = JWTManager(app)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


# Implement the /auth endpoint
@app.route('/auth', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = UserModel.find_by_username(username)
    if user and user.password == password:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


if __name__ == '__main__':
    from section7.startercode.db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
