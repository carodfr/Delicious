from app.db import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    quantity = db.Column(db.Integer())
    description = db.Column(db.String(200))
    minutes_preparation = db.Column(db.Integer())
    image_path = db.Column(db.String(80))

    def __init__(self, name, price, quantity, description, minutes_preparation,image_path):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.minutes_preparation = minutes_preparation
        self.image_path=image_path

    def json(self):
        return {'name': self.name, 'price': self.price, 'quantity': self.quantity, 'image_path': self.image_path}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
