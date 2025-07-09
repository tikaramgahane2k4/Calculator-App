from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # secure key for session

@app.route("/", methods=["GET", "POST"])
def calculator():
    if "display" not in session:
        session["display"] = ""

    if request.method == "POST":
        btn = request.form.get("btn")

        if btn:
            if btn == "AC":
                session["display"] = ""
            elif btn == "C":
                session["display"] = session["display"][:-1]
            elif btn == "=":
                try:

                    session["display"] = str(eval(session["display"]))
                    
                except:
                    session["display"] = "Error"
            else:
                session["display"] += btn

        return redirect(url_for("calculator"))

    return render_template("index.html", display=session.get("display", ""))



