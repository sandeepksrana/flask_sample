
from flask import Flask
from flask_admin import Admin

app = Flask(__name__)


app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:master@localhost/mydb'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

admin = Admin(app, name='Sri Ram', template_mode='bootstrap3')


from . import models
from . import forms
from . import views
