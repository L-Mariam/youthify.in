from flask import Flask, render_template, session, redirect, flash, request
from admin import checkSession, validateLogin, admin_logout

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

@app.route('/admin/')
def admin():
    checkSession()
    if not session['login']:
        return redirect('/admin/login/')
    return redirect('/admin/dashboard/')

@app.route('/admin/login/')
def adminlogin():
    checkSession()
    if session['login']:
        return redirect('/admin/dashboard/')
    return render_template("login.html")

@app.route('/admin/login/submit', methods=['GET', 'POST'])
def validate_login():
    checkSession()
    if session['login']:
        return redirect('/admin/dashboard/')
    data = request.form
    id, password = data['id'].lower(), data['password']

    return validateLogin(id, password)

@app.route('/admin/logout')
def logout():
    admin_logout()
    return redirect('/admin/login/')


@app.route('/admin/dashboard/')
def admin_dashboard():
    session['login'] = True
    checkSession()
    if not session['login']:
        return redirect("/admin/login/")
    return render_template("dashboard.html")

@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html')

app.run(debug=True)