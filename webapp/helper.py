from flask import current_app
from json import dumps
from os import path, remove
from .models import Writer, Blog
from . import ALLOWED_EXTENSIONS, db

#get user by email
def get_user_email(email):
    return db.session.query(Writer).filter_by(email=email).first()

# get user by id
def get_user_id(id):
    return db.session.query(Writer).filter_by(id=id).first()

# add data to the database
def add_to_database(data):
    db.session.add(data)
    db.session.commit()

# get blog by id
def get_blog(post_id):
    return db.session.query(Blog).filter(Blog.id == post_id).first()

# remove blog from database
def remove_blog(post_id):
    blog = db.session.query(Blog).filter(Blog.id == post_id)
    removed_blog = blog.first()
    # remove the image file from the folder
    if removed_blog.image_file is not None:
        delete_file(path.join(current_app.config['UPLOAD_FOLDER'], add_id(removed_blog.image_file, post_id)))
    blog.delete()
    db.session.commit()

def delete_file(file_path):
    remove(file_path)

def save_file(file, file_path):
    file.save(file_path)

# match into map and serialize content and subtitle into string
def serialize(contents, subtitles):
    map = {}
    for i in range(len(contents)):
        map[subtitles[i]] = contents[i]
    return dumps(map)

# validate if file extension allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def add_id(file_path, id):
    filename, file_extension = path.splitext(file_path)
    return filename + '_' + str(id) + file_extension


# ------------modify data table (careful to use)-----------------
def clear_data(model):
    db.session.query(model).delete()
    db.session.commit()

def delete_user(email):
    db.session.query(Writer).filter_by(email=email).delete()
    db.session.commit()

def list_user():
    users = db.session.query(Writer).all()
    for user in users:
        print(user.email)
