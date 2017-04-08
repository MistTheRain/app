"""
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask import Flask
app = Flask(__name__)


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    #remember_me = BooleanField('remember_me', default=False)
	
	
@app.route("/")
def hello():
    #lat, long = main()
    return LoginForm #"Hello World! %s %s" % (lat, long)

if __name__ == "__main__":
    app.run()


from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# index view function suppressed for brevity

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
						   
"""


from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Flask
app = Flask(__name__)


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)
	
if __name__ == "__main__":
    app.run()




