from app.db import db
from passlib.hash import pbkdf2_sha512

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    users = db.relationship('User', lazy='dynamic')

    def __init__(self, _id, name):
        self.id = _id
        self.name = name

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
        cls(1,'Administrator').save_to_db()
        cls(2,'Client').save_to_db()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(130))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    address = db.Column(db.String(80))

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role')

#    orders = db.relationship('Order', lazy='dynamic')

    def __init__(self, username, password, firstname, lastname, address):
        self.username = username
        self.password = pbkdf2_sha512.encrypt(password)
        self.firstname = firstname
        self.lastname = lastname
        self.address = address

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def check_login(cls, username):
        return cls.query.filter_by(username=username, password=pbkdf2_sha512.encrypt(password)).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def init_data(cls):
        cls('admin', '123456', '-', '-', '-').save_to_db()

