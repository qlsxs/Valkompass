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
    if(subcategory == None):
        return redirect("/home")
    candidates = []
    for cand in subcategory["candidates"]:
        candidates.append({"name": cand["name"], "year": cand["year"], "pfp": cand["pfp"]})
    return render_template("category.html", subcategory = subcategory, candidates = candidates, url = cat)

@app.route("/category/<cat>/questions/<id>")
def load_question(cat, id):
    if("scores" in session):
        print(type(session["scores"]))
    if(not id.isnumeric() and not id == "last"):
        return redirect("/category/" + cat)
    else:
        if(id == "last"):
            id = -1
        subcategory, candidates, question, id = data.get_data_for_question(cat, int(id))
        if(subcategory == None):
            return redirect("/home")
        elif(question == "Max"):
            return redirect("/category/" + cat + "/summary")
        else:     
            return render_template("question.html", subcategory = subcategory, candidates = candidates, question = question, id = int(id), url = cat)

@app.route("/category/<cat>/summary")
def show_summary(cat):
    subcategory = data.get_subcategory(cat)
    return render_template("summary.html", subcategory = subcategory, url = cat)

@app.route("/category/<cat>/candidate/<id>")
def load_candidate_profile(cat, id):
    subcategory = data.get_subcategory(cat)
    try:
        candidate = subcategory["candidates"][int(id)]
        return render_template("candidate.html", cat_name = subcategory["name"], questions = subcategory["questions"], candidate = candidate, url=cat)
    except:
        return redirect("/category/" + cat)
    
@app.route("/update_session_score", methods=["POST"])
def update_session_score():
    data = request.get_json()
    key = "score" + "-" + str(data["cat"]) + "-" + str(data["question_id"])
    session[key] = data["score"]
    return "true"
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