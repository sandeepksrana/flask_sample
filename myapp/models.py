from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

from . import app, admin


db = SQLAlchemy(app)



class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80),unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), unique=True, nullable=False)

	def __repr__(self):
		return '<User %r>' % self.name



admin.add_view(ModelView(User, db.session))
