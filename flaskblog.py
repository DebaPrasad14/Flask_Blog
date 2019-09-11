from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__=='__main__':
	app.run(debug=True)