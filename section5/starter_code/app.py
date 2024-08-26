import os  # for access to environment variables

from flask import Flask
from flask_restful import Api

from section5.starter_code.resources.item import Item, ItemList
from section5.starter_code.resources.store import Store, StoreList


app = Flask(__name__)  # created an app

app.config['DEBUG'] = True  # debug flag (for testing)
# saving data into the config flag. = environment var DATABASE_URL that's set on my pc.
# .get: if the var is not set, the link will be used as a default value
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)  # created an api

api.add_resource(Item, '/item/<string:name>')  # added resource and specified the endpoint structure
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request  # if in debug mode, creating tables only before first request
        def create_tables():  # created tables
            db.create_all()

    app.run(port=5000)
