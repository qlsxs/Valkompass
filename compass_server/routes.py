from compass_server import app
from flask import request, session, flash, redirect, url_for, render_template, abort
import os, json
import uuid
import compass_server.data as data

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html", categories = data.get_all_categories())

@app.route("/category/<cat>")
def load_category(cat):
    subcategory = data.get_subcategory(cat)
    candidates = []
    for cand in subcategory["candidates"]:
        candidates.append({"name": cand["name"], "year": cand["year"], "pfp": cand["pfp"]})
    return render_template("category.html", subcategory = subcategory, candidates = candidates, url = cat)

# WE HAVE UPDATED THE DATA SYSTEM, REMAKE THESE THINGS

@app.route("/questions/<cat>/<id>")
def load_question(cat, id):
    if(not id.isnumeric()):
        return redirect("/category/" + cat)
    else:
        subcategory, candidates = data.get_subcategory_and_candidates(cat)
        if(subcategory == None):
            return redirect("home.html", categories = data.get_all_categories())
        question = data.get_question(cat, int(id))
        if(question == None):
            return redirect("/category/" + cat)
        elif(question == "Max"):
            return redirect("/summary/" + cat)
        else:     
            answers = data.get_candidate_answers_for_question(cat, int(id))
            return render_template("question.html", subcategory = subcategory, candidates = candidates, question = question, id = int(id), url = cat, answers = answers)

@app.route("/summary/<cat>")
def show_summary(cat):
    subcategory, candidates = data.get_subcategory_and_candidates(cat)
    return render_template("summary.html", subcategory = subcategory, candidates = candidates)
# @app.route("/newuser", methods=["GET", "POST"])
# def newuser():
#     if(request.method == "POST"):
#         name = request.form["username"]
#         if(username_exists(name)):
#             flash("Användarnamet är upptaget!", "warning")
#             return render_template("createuser.html", form = SignUpForm())
#         password = request.form["password"]
#         password_hash = bcrypt.generate_password_hash(password, __ROUNDS)
#         data = (name, password_hash)
#         conn = create_connection()
#         cur = conn.cursor()
#         # Check is done twice since otherwise you can spam click the submit button to get multiple with same user
#         # Doing it twice prevents the large timesink from the hashing
#         if(username_exists(name)):
#             flash("Användarnamet är upptaget!", "warning")
#             return render_template("createuser.html", form = SignUpForm())
#         cur.execute("INSERT INTO users (username, password) VALUES (?,?)", data)
#         conn.commit()
#         conn.close()
#         flash("Kontot har skapats!", "success")
#         return redirect("index")
#     else:
#         return render_template("createuser.html", form = SignUpForm())