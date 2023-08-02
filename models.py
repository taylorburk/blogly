"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                     nullable=False)
    last_name = db.Column(db.String(50),
                     nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.Text,
                     nullable=False)
    content = db.Column(db.Text,
                     nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now, nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class PostTag(db.Model):
    __tablename__ = "posts_tag"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'),
                   primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'),
                   primary_key=True)

class Tag(db.Model):
    __tablename__='tag'

    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    post = db.relationship('Post',secondary="posts_tag",backref="tags")