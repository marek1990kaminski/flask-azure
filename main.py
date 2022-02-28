from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@micro-main-db/main'
db: SQLAlchemy = SQLAlchemy(app)
