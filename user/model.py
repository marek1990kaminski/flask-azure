from dataclasses import dataclass

from main import db


@dataclass
class User(db.Model):
    id: int
    text: str
    deleted: bool
    done: bool

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(200))
    text = db.Column(db.String(200))
    deleted = db.Column(db.Boolean())
    done = db.Column(db.Boolean())
