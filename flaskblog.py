from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	
	{
		'author':'Dev',
		'title':'Blog 1'
	},
	{
		'author':'Shree',
		'title':'Blog 2'
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