from config import db
from flask import session, flash, redirect

cursor = db.cursor()

def checkSession():
    try:
        if not session['login']:
            session['login'] = False
            session["user"] = ""
    except KeyError:
        session['login'] = False
        session["user"] = ""

def validateLogin(id, password):
    query = "SELECT * FROM admin WHERE admin_id = %s;"
    try:
        cursor.execute(query, (id))
        result = cursor.fetchall()
        if len(result) == 1:
            if result[0][1] == password:
                session['login'] = True
                session['user'] = id
                flash("Logged In Successfully", "green")
                return redirect("/admin/dashboard/")
            else:
                flash("Incorrect ID or Password", "red")
                session['login'] = False
                session['user'] = ""
                return redirect("/admin/login/")
        return redirect("/admin/login/")
    except:
        return redirect("/admin/login/")

def admin_logout():
    session['login'] = False
    session['user'] = ""