from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e43229aeb54fa2017b4d773e44aef0dd'

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
def home():
	return render_template('home.html', posts=posts)


@app.route("/about")
def about():
	return render_template('about.html', title='about')

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)


if __name__=='__main__':
	app.run(debug=True)