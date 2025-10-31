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
    candidates_primitive = data.get_subcat_candidates(cat)
    candidates_condensed = []
    for cand in candidates_primitive:
        candidates_condensed.append({"name": cand["name"], "year": cand["year"], "pfp": cand["pfp"]})
    if(loadEnglish(cat)):
        return render_template("engCategory.html", subcategory = subcategory, candidates = candidates_condensed, url = cat)
    return render_template("category.html", subcategory = subcategory, candidates = candidates_condensed, url = cat)

@app.route("/category/<cat>/questions/<id>")
def load_question(cat, id):
    if(not id.isnumeric() and not id == "-1"):
        return abort(404)
    else:
        if(id == "-1"):
            return redirect(url_for("load_category", cat = cat))
        subcategory, candidates, question, id = data.get_data_for_question(cat, int(id))
        if(subcategory == None):
            return abort(404)
        elif(question == "Max"):
            return redirect(url_for("show_summary", cat = cat))
        else: 
            if(loadEnglish(cat)):
                return render_template("engQuestion.html", subcategory = subcategory, candidates = candidates, question = question, id = int(id), url = cat)
            return render_template("question.html", subcategory = subcategory, candidates = candidates, question = question, id = int(id), url = cat)

@app.route("/category/<cat>/summary")
def show_summary(cat):
    subcategory = data.get_subcategory(cat)
    candidates = data.get_subcat_candidates(cat)
    if(subcategory == None):
        return abort(404)
    if(loadEnglish(cat)):
        return render_template("engSummary.html", subcategory = subcategory, candidates = candidates, url = cat)
    return render_template("engSummary.html", subcategory = subcategory, candidates = candidates, url = cat)

@app.route("/category/<cat>/candidate/<id>")
def load_candidate_profile(cat, id):
    candidate = data.get_candidate(cat, int(id))
    if(loadEnglish(cat)):
        return render_template("engCandidate.html", candidate = candidate, url=cat)
    return render_template("candidate.html", candidate = candidate, url=cat)
   
    
@app.route("/update_session_score", methods=["POST"])
def update_session_score():
    data = request.get_json()
    key = "score" + "-" + str(data["cat"]) + "-" + str(data["question_id"])
    session[key] = data["score"]
    return "true"

@app.route("/random_subcategory")
def random_subcategory():
    return redirect(url_for("load_category", cat = data.get_random_subcategory()))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def loadEnglish(cat):
    return cat.split("-")[0]=="fint"