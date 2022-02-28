from dataclasses import dataclass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@azure-postgres-db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db: SQLAlchemy = SQLAlchemy(app)


@dataclass
class ToDoTask(db.Model):
    id: int
    user_id: str
    text: str
    deleted: bool
    done: bool

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(200))
    text = db.Column(db.String(200))
    deleted = db.Column(db.Boolean())
    done = db.Column(db.Boolean())


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
