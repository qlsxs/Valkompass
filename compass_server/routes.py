from compass_server import app
from flask import request, session, redirect, url_for, render_template, abort
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
        return abort(404)
    candidates = []
    for cand in subcategory["candidates"]:
        candidates.append({"name": cand["name"], "year": cand["year"], "pfp": cand["pfp"]})
    return render_template("category.html", subcategory = subcategory, candidates = candidates, url = cat)

@app.route("/category/<cat>/questions/<id>")
def load_question(cat, id):
    if("scores" in session):
        print(type(session["scores"]))
    if(not id.isnumeric()):
        return abort(404)
    else:
        subcategory, candidates, question, id = data.get_data_for_question(cat, int(id))
        if(subcategory == None):
            return abort(404)
        elif(question == "Max"):
            return redirect(url_for("show_summary", cat = cat))
        else:     
            return render_template("question.html", subcategory = subcategory, candidates = candidates, question = question, id = int(id), url = cat)

@app.route("/category/<cat>/summary")
def show_summary(cat):
    subcategory = data.get_subcategory(cat)
    if(subcategory == None):
        return abort(404)
    return render_template("summary.html", subcategory = subcategory, url = cat)

@app.route("/category/<cat>/candidate/<id>")
def load_candidate_profile(cat, id):
    subcategory = data.get_subcategory(cat)
    try:
        candidate = subcategory["candidates"][int(id)]
        return render_template("candidate.html", cat_name = subcategory["name"], questions = subcategory["questions"], candidate = candidate, url=cat)
    except:
        return abort(404)
    
@app.route("/update_session_score", methods=["POST"])
def update_session_score():
    data = request.get_json()
    key = "score" + "-" + str(data["cat"]) + "-" + str(data["question_id"])
    session[key] = data["score"]
    return "true"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404