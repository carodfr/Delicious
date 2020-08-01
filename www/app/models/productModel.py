from app.db import db

class ProductType(db.Model):
    __tablename__ = 'product_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(80))

    products = db.relationship('Product', lazy='dynamic')

    def __init__(self, _id, name, description):
        self.id=_id
        self.name = name
        self.description = description

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def init_data(cls):
        cls(1, "Food", "To calm the hunger").save_to_db()
        cls(2, "Drinks", "To refresh yourself").save_to_db()
        cls(3, "Desserts", "At last").save_to_db()

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    quantity = db.Column(db.Integer())
    description = db.Column(db.String(200))
    minutes_preparation = db.Column(db.Integer())
    image_path = db.Column(db.String(80))

    product_type_id = db.Column(db.Integer, db.ForeignKey('product_types.id'))
    product_type = db.relationship('ProductType')

#    orders = db.relationship('Order', lazy='dynamic')

    def __init__(self, product_type_id, name, price, quantity, description, minutes_preparation,image_path):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.minutes_preparation = minutes_preparation
        self.image_path=image_path
        self.product_type_id=product_type_id

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def init_data(cls):
        cls(1, "Hamburger", 6.5, 10, "A 150Gr grilled meat hamburger. The dish comes with potatoes and salad", 15, "/images/hamburger.jpg").save_to_db()
        cls(2, "Lemonade", 1.5, 7, "250cc limonade", 15, "/images/lemonade.jpg").save_to_db()
        cls(3, "icecream", 2, 7, "Vanille ice cream with or baked cake", 14, "/images/icecream.jpg").save_to_db()

