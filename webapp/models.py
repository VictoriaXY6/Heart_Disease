from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from . import db

class Writer(UserMixin, db.Model):
    __tablename__ = 'writers'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    blogs = db.relationship("Blog")

    def __repr__(self):
        return '<Writer %r>' % self.name

    def __init__(self, email, password, name):
        self.email = email
        self.password = generate_password_hash(password, method='sha256')
        self.name = name

class Blog(db.Model):
    __tablename__ = 'blog'
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), nullable=False)
    updated_date = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), nullable=False)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return '<Blog %r>' % self.title

    def __init__(self, writer_id, title, content, image_file):
        self.writer_id = writer_id
        self.title = title
        self.content = content
        if image_file != '':
            self.image_file = image_file
