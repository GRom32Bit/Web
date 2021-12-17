from flask import Flask
from flask import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres: MadNess19@localhost/Web'
db = SQLAlchemy(app)

from app import routes
