from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
load_dotenv()

db = SQLAlchemy()
migrate = Migrate() 

def create_database():
    db.create_all()
    print('Database Created')

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


    db.init_app(app)
    migrate.init_app(app,db)

    from .views import views_bp

    app.register_blueprint(views_bp,url_prefix="/")


    # with app.app_context():
        
    #     create_database()

    
    return app