from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post



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
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Your Account has been created! You are now able to log in', 'success')
		return redirect(url_for('login'))

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