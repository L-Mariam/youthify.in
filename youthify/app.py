from flask import Flask, render_template, session, redirect, flash, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "youthify"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/blogs/')
def blogs():
    return render_template("blogs.html")

@app.route('/blog/<post_id>/')
def blog(post_id):
    return render_template("blogpost.html", post_id=post_id)

@app.route('/events/')
def events():
    return render_template("events.html")

@app.route('/team/')
def team():
    return render_template("team.html")


@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html')

app.run(debug=True)