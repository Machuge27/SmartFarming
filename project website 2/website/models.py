from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    arduino_data = db.relationship('Arduino_data',backref='user')
    messages=db.relationship('Messages',backref='author')
    sensor_data=db.relationship('Sensor_data',backref='sensor')
    average_temp=db.relationship('Average_Temp',backref='average')
    
class Arduino_data(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_relation = db.Column(db.Integer, db.ForeignKey('user.id'))

class Sensor_data(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    temp=db.Column(db.Integer)
    humidity=db.Column(db.Integer)
    moisture=db.Column(db.Integer)
    date=db.Column(db.DateTime(timezone=True), default=func.now())
    user_relation=db.Column(db.Integer,db.ForeignKey('user.id'))

class Messages(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_relation = db.Column(db.Integer, db.ForeignKey('user.id'))

class Average_Temp(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    avg_temp=db.Column(db.Integer)
    avg_date=db.Column(db.Integer)
    avg_humidity=db.Column(db.Integer)
    avg_moisture=db.Column(db.Integer)
    created=db.Column(db.DateTime(timezone=True),default=func.now())
    user_relation=db.Column(db.Integer,db.ForeignKey('user.id'))