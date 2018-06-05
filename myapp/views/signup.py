
from flask import render_template,request,redirect,flash,url_for

from .. import app
from ..models import User, db
from ..forms import SignupForm

@app.route('/showSignUp',methods=['GET','POST'])
def showSignUp():
	form = SignupForm(request.form)
	if request.method == 'POST' and form.validate():
		user = User(name=form.name.data,email=form.email.data,password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Thanks for registering')
		return redirect(url_for('admin.index'))

	return render_template('signup.html',form=form)



