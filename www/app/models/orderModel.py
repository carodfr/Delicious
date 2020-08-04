from app.db import db

from sqlalchemy.sql import func

from app.models.productModel import Product

class OrderStatus(db.Model):
    __tablename__ = 'order_status'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80))

    orders = db.relationship('Order', lazy='dynamic')

    def __init__(self, _id, status):
        self.id=_id
        self.status = status

    @classmethod
    def find_by_status(cls, status):
        return cls.query.filter_by(status=status).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def init_data(cls):
        cls(1,'Being prepared').save_to_db()
        cls(2,'In route').save_to_db()
        cls(3,'Delivered').save_to_db()


class ProductOrdered(db.Model):
    __tablename__ = 'products_ordered'

    id = db.Column(db.Integer, primary_key=True)
    product_quantity = db.Column(db.Integer)

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    order = db.relationship('Order')

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship('Product')

    def __init__(self, order_id, product_id, product_quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.product_quantity = product_quantity

    @classmethod
    def find_by_order_id(cls, order_id):
        return cls.query.filter_by(order_id=order_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


 
class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_firstname = db.Column(db.String(80))
    customer_lastname = db.Column(db.String(80))
    customer_address = db.Column(db.String(80))
    date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    total = db.Column(db.Float(precision=2))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')

    products_ordered = db.relationship('ProductOrdered', lazy='dynamic')

    order_status_id = db.Column(db.Integer, db.ForeignKey('order_status.id'))
    order_status = db.relationship('OrderStatus')

    def __init__(self, customer_firstname, customer_lastname, customer_address, user_id):
        self.customer_firstname=customer_firstname
        self.customer_lastname=customer_lastname
        self.customer_address=customer_address
        self.total=0
        self.user_id=user_id
        self.order_status_id=1 # the first state

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        return cls.query.order_by(cls.date.desc()).all()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).order_by(cls.date.desc())

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_product(self, product_id, product_quantity):
        if(self.id==None):
            self.save_to_db()
        self.total+=Product.find_by_id(product_id).price * quantity
        self.save_to_db()
        ProductOrdered(self.id, product_id, product_quantity).save_to_db()

    def promote_status(self):
        if self.order_status_id<3:
            self.order_status_id+=1
            self.save_to_db()
