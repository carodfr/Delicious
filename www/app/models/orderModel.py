from app.db import db

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


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_firstname = db.Column(db.String(80))
    customer_lastname = db.Column(db.String(80))
    customer_address = db.Column(db.String(80))
    date = db.Column(db.Date)
    total = db.Column(db.Float(precision=2))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users')

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    products = db.relationship('products.id')

    order_status_id = db.Column(db.Integer, db.ForeignKey('order_status.id'))
    status = db.relationship('order_status.id')

    def __init__(self, customer_firstname, customer_lastname, customer_address, date, total, user_id, product_id):
        self.customer_firstname=customer_firstname
        self.customer_lastname=customer_lastname
        self.customer_address=customer_address
        self.date=date
        self.total=total
        self.user_id=user_id
        self.product_id=product_id
        self.order_status_id=1 # the first state

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
