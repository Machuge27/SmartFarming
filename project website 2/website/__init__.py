#__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_socketio import SocketIO

db=SQLAlchemy()
DB_NAME="database.db"

#assighning to socketio
socketio=SocketIO()

def create_app():
  app=Flask(__name__)
  app.config['SECRET_KEY']='ALPHA MALE dbhdbhbh'
  app.config['SQLALCHEMY_DATABASE_URI']=f"sqlite:///{DB_NAME}"

  #initialize SQLALCHEMY with the flask app
  db.init_app(app)
  #initialize SocketIO with the Flask app
  socketio.init_app(app)

  #import blueprints
  from .views import views
  from .auth import auth

  #register blueprints
  app.register_blueprint(views,url_prefix='/')
  app.register_blueprint(auth,url_prefix='/')

  # import models
  #ive imported all models using form . import models
  from .models import User
  from .models import Sensor_data
  from .models import Arduino_data
  from .models import Messages
  from .models import Average_Temp

  #create database if it doesnt exists
  create_database(app)

  #configure flask login
  login_manager=LoginManager()
  login_manager.login_view="auth.login"
  login_manager.init_app(app)

  # Define the user loader function for Flask-Login
  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))
  
  return app

def create_database(app):
  if not path.exists(DB_NAME):
   with app.app_context():
    db.create_all()
    print("created database")


