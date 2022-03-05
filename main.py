from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@azure-postgres-db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db: SQLAlchemy = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
