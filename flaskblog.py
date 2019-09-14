from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'e43229aeb54fa2017b4d773e44aef0dd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import User, Post



posts = [
	{
		'author':'Dev',
		'title':'Blog 1',
		'date_posted': '05 sept 2019',
		'content': 'This is the first blog content'
	},
	{
		'author':'Shree',
		'title':'Blog 2',
		'date_posted': '07 sept 2019',
		'content': 'This is the second blog content'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)


@app.route("/about")
def about():
	return render_template('about.html', title='about')


@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()

	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))

	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		if form.email.data=='dev@gmail.com' and form.password.data=='dev':
			flash(f'You have logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash(f'Log in unsuccessful!', 'danger')

	return render_template('login.html', title='Login', form=form)


if __name__=='__main__':
	app.run(debug=True)