from section5.starter_code.db import db


class ItemModel(db.Model):
    __tablename__ = 'items'
    # defining columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))  # 80 is max num of characters
    price = db.Column(db.Float(precision=2))  # .23

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))  # diff table. store_id is a foreign key
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # returning an item object model

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()  # saving the changes

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
