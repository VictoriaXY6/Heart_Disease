from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
from .chart_generator import generate_data, process_data

# init SQLAlchemy to use later for our models
db = SQLAlchemy()

# generate data and list of data for the charts page
data = generate_data()
data_list = process_data(data)

UPLOAD_FOLDER = 'webapp/blog/static/blog_imgs'
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif'}

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    from .helper import add_id
    # update globally to add add_id method into jinja
    app.jinja_env.globals.update(add_id=add_id)

    # note: need to run following command to create database in terminal
    # from webapp import db, create_app
    # db.create_all(app=create_app())

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import Writer

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return db.session.query(Writer).get(int(user_id))

    # blueprint for auth routes in our app
    from .auth.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for blog parts of app
    from .blog.blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    app.register_error_handler(404, page_not_found)

    return app

def page_not_found(e):
  return render_template('errors/404.html', page_title='Page Not Found'), 404
