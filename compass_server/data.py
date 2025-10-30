import random
from compass_server.read_data import categories, candidates, get_subcategory as get_subcategory_primitive

def get_all_categories():
    # Returns every post/subcategory
    subcats = []
    for category in categories:
        subcats.append(condense_category(category))
        for subcategory in category["subcategories"]:
            subcats.append(condense_category(subcategory))
    return subcats

def condense_category(cat):
    if("id" in cat.keys()):
        return {"name": cat["name"], "src": cat["src"], "id":cat["id"]}
    return {"name": cat["name"], "src": cat["src"]}

def get_subcategory(cat):
    return get_subcategory_primitive(cat, categories)

def get_subcat_candidates(cat):
    subcat_cands = []
    for candidate in candidates:
        if(candidate["subcategory"] == cat):
            subcat_cands.append(candidate)
    return subcat_cands

def get_data_for_question(cat, i):
    # Returns everything neccesary to display the i:th question for the category cat
    category = get_subcategory(cat)
    if (category == None):
        return None, None, None, None
    candidates = get_subcat_candidates(cat)
    if (i == -1):
        i = len(category["questions"])-1
    if (i < 0 or i > len(category["questions"])):
        return None, None, None, None
    if (i == len(category["questions"])):
        return "Max", "Max", "Max", "Max"
    condensed_candidates = []
    for cand in candidates:
        # only display the data for the relevant question, send less stuff
        condensed_candidates.append({"name": cand["name"], "year": cand["year"],
                          "pfp": cand["pfp"], "answer": cand["answers"][i]})
    return {"name": category["name"], "desc": category["desc"], "src": category["src"]}, condensed_candidates, category["questions"][i], i

def get_candidate(cat, id):
    # Returns everything about a candidate, since there is one candidate with two pfp:s (whyyyy), the category determines which pfp gets used
    candidate_temp = get_subcat_candidates(cat)[id]
    duplicates = []
    for cand in candidates:
        if(cand["name"] == candidate_temp["name"]):
            duplicates.append(cand)
    candidate = {"name": candidate_temp["name"], "year": candidate_temp["year"], "subcategories": [], "pfp": candidate_temp["pfp"], "answers_list": [], "questions_list": []}
    for dupe in duplicates:
        dupe_subcat = get_subcategory(dupe["subcategory"])
        candidate["subcategories"].append(dupe_subcat["name"])
        candidate["answers_list"].append(dupe["answers"])
        candidate["questions_list"].append(dupe_subcat["questions"])
    return candidate

def get_random_subcategory():
    # Returns a random subcategory
    num_of_subcats = 0
    for cat in categories:
        num_of_subcats += len(cat["subcategories"])

    index = random.randint(0, num_of_subcats-1)
    current_index = 0
    while (index >= 0):
        cat = categories[current_index]["subcategories"]
        if (len(cat) > index):
            return cat[index]["src"]
        index -= len(cat)
        current_index += 1
    return categories[current_index]["subcategories"][index]["src"]
