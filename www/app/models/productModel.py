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

    #orders = db.relationship('Order', lazy='dynamic')

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
        cls(1, "Hamburger", 6, 10, "A 150Gr grilled meat hamburger. Comes with french fries and salad.", 15, "/images/hamburger.jpg").save_to_db()
        cls(1, "Chicken", 7, 10, "A 300Gr breaded chicken. comes with potatoes and salad", 15, "/images/chicken.jpg").save_to_db()
        cls(1, "Paella", 9, 10, "Perfect for the seafood lovers, it comes with oysters and mussels", 15, "/images/paella.jpg").save_to_db()
        cls(1, "Ribs", 12, 10, "300Gr Ribs. Comes with french fries.", 15, "/images/ribs.jpg").save_to_db()
        cls(1, "Salmon", 12, 10, "Chilean salmon. Comes with vegetables.", 15, "/images/salmon.jpg").save_to_db()
        cls(1, "Wrap", 7, 10, "Wrap with chicken and salad.", 15, "/images/wrap.jpg").save_to_db()
        
        cls(2, "Soda", 2, 7, "250cc soda. The soda comes with pieces of fruit.", 5, "/images/soda.jpg").save_to_db()
        cls(2, "Juice", 3, 7, "330cc juice. Made of tropical fruits.", 9, "/images/juice.jpg").save_to_db()
        cls(2, "Tee", 3, 7, "200cc Tee.", 12, "/images/tee.jpg").save_to_db()
        cls(2, "Beer", 2, 7, "500cc Beer.", 3, "/images/beer.jpg").save_to_db()
       
        cls(3, "Pancakes", 4, 7, "Baked pancakes with syrup or honey", 12, "/images/pancakes.jpg").save_to_db()
        cls(3, "Macaroons", 3, 7, "Try our special macaroon recipe.", 3, "/images/macaroons.jpg").save_to_db()
        cls(3, "Forest fruit Cake", 3, 7, "This cake has a great variety of forest fruits, such as  blackberries and raspberries.", 5, "/images/cake.jpg").save_to_db()

