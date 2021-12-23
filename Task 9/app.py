from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
import os
import json
from flask_swagger_ui import get_swaggerui_blueprint
from flask_login import LoginManager
from enum import Enum

with open('data.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'

app.config['JWT_BLACKLIST_ENABLED'] = False
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

# swagger config
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUE_PRINT = get_swaggerui_blueprint(SWAGGER_URL,
                                             API_URL,
                                             config={
                                                 'app_name': "Contracts"
                                             })
db = SQLAlchemy(app)
jwt = JWTManager(app)
ma = Marshmallow(app)
app.register_blueprint(SWAGGER_BLUE_PRINT, url_prefix=SWAGGER_URL)
login_manager = LoginManager(app)


class AccessRights(Enum):
    ADMIN = "admin"
    USER = "user"




