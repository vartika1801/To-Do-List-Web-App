from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create database
db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    
    app.config['SECRET_KEY']='your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' # db address 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    
    # to connect db object to app
    db.init_app(app)
    
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    
    return app
    