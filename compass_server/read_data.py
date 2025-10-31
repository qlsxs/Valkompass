import csv

def get_subcategory(cat, categories):
    # Returns the subcategory with src cat
    for i in range(0, len(categories)):
        for j in range(0, len(categories[i]["subcategories"])):
            if (categories[i]["subcategories"][j]["src"] == cat):
                return categories[i]["subcategories"][j]

def get_correct_subcat(candidate_count, subcats, name):
    # Some people are applying for multiple posts, find the correct one for this instance of the person, which are treated differently here.
    subcats_list = comma_split(subcats)
    s = correct_name(subcats_list[candidate_count[name]].strip())
    return s
    
def comma_split(str):
    # Splits like a normal .split on comma, but ignores if it is in parenthesis
    par = 0
    last_index = 0
    substrings = []
    for i in range(0,len(str)):
        s = str[i]
        if(s == "("):
            par += 1
        elif(s == ")"):
            par -= 1
        elif(s == "," and par == 0):
            substrings.append(str[last_index:i])
            last_index = i+1
    substrings.append(str[last_index:])
    return substrings


def update_candidate_count(candidate_count, name):
    # Keeps track of how many times a certain candidate has been seen (to deal with people applying to multiple posts), shifted by 1 for no reason (or rather a stupid reason that isnt valid)
    if(name in candidate_count.keys()):
        candidate_count[name] += 1
    else:
        candidate_count[name] = 0

def subcat_exists(subcategories, subcat_candidate):
    for subcat in subcategories:
        if(subcat["name"] == subcat_candidate):
            return True
    return False

def correct_name(name):
    # Changes the questionairre format name into the proper name
    match name:
        case "Ordförande (Styret)":
            return "styret-ordforande"
        case "Vice ordförande (Styret)":
            return "styret-viceordforande"
        case "Kassör (Styret)":
            return "styret-kassor"
        case "Studiesocialt ansvarig ledamot (Styret)":
            return "styret-sso"
        case "Ledamot (Styret) [3 st.]":
            return "styret-ledamot"
        case "Generalsekreterare [2 st.]":
            return "fn-ordforande"
        case "Portföljförvaltare":
            return "fn-portsfoljforvaltare"
        case "Samordnare för arbetsmarknadsdagen (Fusionsreaktor 2026)":
            return "fn-fusionsreaktor"
        case "Samordnare för arbetsmarknadsdagen (Fusionsreaktor 2027)":
            return "fn-fusionsreaktor"
        case "Studienämndens ordförande (SNO)":
            return "fsn-sno"
        case "Programansvarig student Teknisk Fysik (F-PAS)":
            return "fsn-fpas"
        case "Jämlikhetsnämnden ordförande (oJämN)":
            return "jamn-ojamn"
        case "Aktivitetsnämndens ordförande (oFAN)":
            return "fan-ofan"
        case "Lokalnämndens ordförande (Generalkonsul, GK)":
            return "frum-gk"
        case "Lokalnämndens kassör (Chargé d'Affaires, CdA)":
            return "frum-cda"
        case "Kommunikationsnämndens ordförande":
            return "fcom-ordforande"
        case "Webmaster":
            return "fcom-webmaster"
        case "Designansvarig":
            return "fcom-design"
        case "Klubbmästare [3 st.]":
            return "fkm-klubbmastare"
        case "Fadderist [4 st.]":
            return "mottagningen-fadderist"
        case "Föhsare [3 st.]":
            return "mottagningen-fohsare"
        case "Ordförande för den internationella nämnden (FINTO)":
            return "fint-president"
        case "Arrangör av Vårbalen 2026 [3 st.]":
            return "varbal-arrangor"
        case "Revisor [2 st.]":
            return "revisor-revisor"
        case "Stabsledning [3 st.]":
            return "fysikalen-stabsledning"
    return ""
            
def read_question_scales():
    lines = []
    with open('compass_server/static/questionScaleData.csv', mode = "r", encoding="utf-8") as file:
        csvFile = csv.reader(file)
        for i,line in enumerate(csvFile):
            if(not i == 0):
                # Add filler to make the questions in the doc align
                line.insert(0, "filler")
                lines.append(line)
            
    return lines

def read_data(categories):
    people = []
    with open('compass_server/static/data.csv', mode ='r', encoding='utf-8') as file:
    # I dont want to explain any of this
        csvFile = csv.reader(file)
        query = None
        people = []
        for i, line in enumerate(csvFile):
            if(i == 0):
                query = line
            else:
                people.append(line)
    candidates = []
    candidate_count = {}
    current_subcat = ""
    scales = read_question_scales()
    for person in people:
        new_subcategory = False
        candidate = {}
        candidate["name"] = person[1].strip()
        candidate["year"] = person[2]
        update_candidate_count(candidate_count, candidate["name"])
        candidate["subcategory"] = get_correct_subcat(candidate_count, person[3], candidate["name"])    
        pfp = candidate["name"]
        if(pfp == "Marcus Joyce"): 
        # Since there is only two people with multiple pfps (whyy), ill just add this as a very specific if statement. I dont have time to make a good solution rn anyway
            if(candidate["subcategory"] == "fkm-klubbmastare"):
                pfp = pfp + " (Klubbis)"
            else:
                pfp = pfp + " (CDA)"
        elif(pfp == "Kristina Torell"):
            if(candidate["subcategory"] == "jamn-ojamn"):
                pfp = pfp + " (JämN)"
            else:
                pfp = pfp + " (FRum)"
        candidate["pfp"] = pfp + ".jpg"
        if(current_subcat != candidate["subcategory"]):
            current_subcat = candidate["subcategory"]
            new_subcategory = True
        candidate["answers"] = []
        for i in range(4, len(query), 2):
            subcat = None
            if(new_subcategory):
                subcat = get_subcategory(candidate["subcategory"], categories)
            if(person[i] != ""):
                candidate["answers"].append({"value": int(person[i]), "reason": person[i+1]})
                if(new_subcategory):
                    subcat["questions"].append({"question": query[i], "lowerScale": scales[0][int(i/2)], "upperScale": scales[1][int(i/2)]})
        candidates.append(candidate)
    return candidates, categories
            
prelim_categories = [
    {
        "name": "Styret",
        "src": "#",
        "id": 0,
        "subcategories": [{
            "name": "Sektionsordförande",
            "desc": "Ordförande har det övergripande ansvaret för sektionen och är ansiktet utåt mot THS och andra sektioner. Ordförande leder också styrelsens arbete under året.",
            "src": "styret-ordforande",
            "amount": 1,
            "questions": []
        },
            {
            "name": "Viceordförande",
            "desc": "Vice ordförande stöttar ordförande i att leda sektionen och tar över om hen inte kan utföra sina uppgifter. Vice ordförande har också en mer administrativ roll som bl.a. innebär att hen sammankallar till möten mellan alla nämnder och har hand om sektionens drive.",
            "src": "styret-viceordforande",
            "amount": 1,
            "questions": []
        },
            {
            "name": "Sektionskassör",
            "desc": "Sektionens kassör är ytterst ansvarig för sektionens ekonomi. Det innebär att hen ansvarar för sektionens budget och stöttar nämnderna i ekonomiska beslut samt bokför alla utgifter och intäkter sektionen som stort har.",
            "src": "styret-kassor",
            "amount": 1,
            "questions": []
        },
            {
            "name": "SSO / Skyddsombud",
            "desc": "SSO är en ledamot med extra ansvar för studiesociala och JML-frågor. Det innebär att hen ska se till att alla är trygga och mår bra på sektionen. Hen ska också vara den person sektionens medlemmar kan komma till och prata om det är något och har därför också tystnadsplikt.",
            "src": "styret-sso",
            "amount": 1,
            "questions": []
        },
            {
            "name": "Styrelseledamot",
            "desc": "Styrelsen har utöver ordförande, vice, kassör och SSO också tre ledamöter som har ansvar för allmänt styrelsearbete och internt fördelar rollerna eventansvarig, näringslivsansvarig, sekreterare och vice kassör. De driver också ofta egna projekt.",
            "src": "styret-ledamot",
            "amount": 3,
            "questions": []
        }]

    },
    {
        "name": "Mottagningen",
        "src": "#",
        "id": 1,
        "subcategories": [{
            "name": "Fadderist",
            "desc": "Fadderisterna är ansvariga för att arrangera sektionens mottagning, de två veckorna i augusti då vi välkomnar alla nyantagna. De har också en teatral roll under mottagningen där de är lite roliga och spexiga.",
            "src": "mottagningen-fadderist",
            "amount": 4,
            "questions": []
        },
            {
            "name": "Föhsare",
            "desc": "Föhsarna är tillsammans med Fadderisterna ansvariga för att arrangera sektionens mottagning, de två veckorna i augusti då vi välkomnar alla nyantagna. De är mottagningens ordförande, vice ordförande och kassör och de har också en teatral roll under mottagningen där de är mystiska och allvetande.",
            "src": "mottagningen-fohsare",
            "amount": 3,
            "questions": []
        }]
    },
    {
        "name": "fkm*",
        "src": "#",
        "id": 2,
        "subcategories": [{
            "name": "Klubbmästare",
            "desc": "Klubbmästarna är ordförande, vice och kassör för klubbmästeriet fkm*. Det innebär att de ansvarar för att arrangera regelbundna pubar och sittningar och ansvarar för all alkoholförsäljning i konsulatet. De rekryterar och leder också alla underansvariga i fkm* som har hand om dekor, mat, märken och dryck på pubar och gasquer.",
            "src": "fkm-klubbmastare",
            "amount": 3,
            "questions": []
        }]
    },
    {
        "name": "FSN",
        "src": "#",
        "id": 3,
        "subcategories": [{
            "name": "SNO",
            "desc": "SNO är ordförande för för studienämnden FSN. Hen sköter det administrativa arbetet i studienämnden och representerar sektionens studenter och deras åsikter mot KTH. SNO fixar också event för studienämnden och har en överblick över deras arbete.",
            "src": "fsn-sno",
            "amount": 1,
            "questions": []
        },
            {
            "name": "F-PAS",
            "desc": "F-PAS är programansvarig student för teknisk fysik och ansvarar därför för kontakt mellan fysikstudenterna och programledningen och examinatorerna när det kommer till studiefrågor. Hen ser till att fysikstudenternas röst hörs när programmet utvecklas.",
            "src": "fsn-fpas",
            "amount": 1,
            "questions": []
        },
            {
            "name": "TM-PAS",
            "desc": "TM-PAS är programansvarig student för teknisk matematik och ansvarar därför för kontakt mellan mattestudenterna och programledningen och examinatorerna när det kommer till studiefrågor. Hen ser också till att mattestudenternas röst hörs när programmet utvecklas. ",
            "src": "fsn-tmpas",
            "amount": 1,
            "questions": []
        }]
    },
    {
        "name": "Fysikalen",
        "src": "#",
        "id": 4,
        "subcategories": [{
            "name": "Stabsledningen",
            "desc": "Stabsledningen är ordförande, vice och kassör för Fysikalen, sektionens så kallade spex (studentikosa musikalteater). De har ansvar för att rekrytera alla gruppchefer som tillsammans leder och skapar spexet. De väljs vartannat år och sitter i två år.",
            "src": "fysikalen-stabsledning",
            "amount": 3,
            "questions": []
        }]
    },
    {
        "name": "FAN",
        "src": "#",
        "id": 5,
        "subcategories": [{
            "name": "Ordförande",
            "desc": "Ordförande för aktivitetsnämnden (oFAN) ansvarar för att leda FAN i sitt arbete genom att bl.a. rekrytera underansvariga som fixar små regelbundna aktiviteter och fixa större event som t.ex.  Åreresan och PAFF.",
            "src": "fan-ofan",
            "amount": 1,
            "questions": []
        }]
    },
    {
        "name": "JämN",
        "src": "#",
        "id": 6,
        "subcategories": [{
            "name": "Ordförande",
            "desc": "Jämlikhetsnämndens ordförande (oJämN) är delvis ansvarig för jämlikhetsarbetet på sektionen och leder jämlikhetsnämndens arbete genom att bl.a. rekrytera underansvariga, hålla lunchmöten och planera aktiviteter som har med jämlikhet att göra.",
            "src": "jamn-ojamn",
            "amount": 1,
            "questions": []
        }]
    },
    {
        "name": "FRum",
        "src": "#",
        "id": 7,
        "subcategories": [{
            "name": "GK (Ordförande)",
            "desc": "GK (Generalkonsul) är ordförande för lokalnämnden FRum. Hen är ansvarig för vår sektionslokal konsulatet och leder tillsammans med CdA FRums arbete genom bl.a. lunchmöten, städdagar och internevent. De rekryterar också underansvariga som bl.a. har ansvar för sektionsbilen.",
            "src": "frum-gk",
            "amount": 1,
            "questions": []
        },
            {
            "name": "CDA (Kassör)",
            "desc": "CdA (Chargé d’Affaires) är kassör för lokalnämnden FRum och ansvarig för godisskåpet i konsulatet. Hen leder tillsammans med GK FRums arbete genom bl.a. lunchmöten, städdagar och internevent. De rekryterar också underansvariga som bl.a. har ansvar för sektionsbilen.",
            "src": "frum-cda",
            "amount": 1,
            "questions": []
        }]
    },
    {
        "name": "FINT",
        "src": "#",
        "id": 8,
        "subcategories": [{
            "name": "President",
            "desc": "FINTo is the head of the international organization in the chapter. They organize meetings, keep in contact with the administration and lead FINT in its day to day work. They are also responsible for the international reception for all exchange students coming to the physics chapter. ",
            "src": "fint-president",
            "amount": 1,
            "questions": []
        }]
    },
    {
        "name": "Fcom",
        "src": "#",
        "id": 9,
        "subcategories": [{
            "name": "Ordförande",
            "desc": "Fcoms ordförande ansvarar för att samordna Fcom och dess delnämnder, The Force, F.Dev och FArt som tillsammans har hand om sektionens kommunikation och informationsspridning. Hen är också ansvarig för generella sektionsmärken, ovverallerna och sångboken.",
            "src": "fcom-ordforande",
            "amount": 1,
            "questions": []
        },
            {
            "name": "Webmaster",
            "desc": "Webmaster är ansvarig för programmeringsgruppen F.Dev som har programmeringsmöten där de ibland jobbar på olika projekt åt resten av sektionen. Webmaster är också ansvarig för sektionens webbplats.",
            "src": "fcom-webmaster",
            "amount": 1,
            "questions": []
        },
            {
            "name": "Redaktör",
            "desc": "Redaktören är ansvarig för sektionstidningen The Force. Hen har hand om att strukturera och publicera tidningen och göra den underhållande både för de som gör den och de som läser.",
            "src": "fcom-redaktor",
            "amount": 1,
            "questions": []
        },
            {
            "name": "Designansvarig",
            "desc": "Designansvarig är ansvarig för designgruppen FArt som fixar märken och annan grafik och grafisk profil till resten av sektionen.",
            "src": "fcom-design",
            "amount": 1,
            "questions": []
        }]
    },
    {
        "name": "FN",
        "src": "#",
        "id": 10,
        "subcategories": [{
            "name": "Ordförande",
            "desc": "Generalsekreteraren är ordförande för näringslivsnämnden FN och leder deras allmänna arbete genom att bl.a. hålla möten, rekrytera underansvariga och ansvarar för annan operativ verksamhet.",
            "src": "fn-ordforande",
            "amount": 1,
            "questions": []
        },
            {
            "name": "Kassör",
            "desc": "FNs kassör är ansvarig för näringslivsnämnden FNs ekonomi och har därför hand om deras budget och ser till att allt bokförs och dokumenteras rätt. FN är en av sektionens större inkomstkällor så det är ett stort ansvar. Hen hjälper också FNs ordförande i att leda nämnden.",
            "src": "fn-kassor",
            "amount": 1,
            "questions": []
        },
            {
            "name": "Portföljförvaltare",
            "desc": "Portföljförvaltaren ansvarar för sektionens kapitalförvaltning (aktiefond) och leder gruppen F.Cap i att bestämma vilka investeringar som ska göras och inte.",
            "src": "fn-portsfoljforvaltare",
            "amount": 1,
            "questions": []
        },
            {
            "name": "Fusionsreaktor",
            "desc": "Fusionsreaktorn är samordnare och arrangör för fysiksektionens arbetsmarknadsmässa FUSION. Det innebär att de rekryterar underansvariga och har en överblick under arbetet med att skapa mässan.",
            "src": "fn-fusionsreaktor",
            "amount": 1,
            "questions": []
        }]
    },
    {
        "name": "Vårbalen",
        "src": "#",
        "id": 11,
        "subcategories": [{
            "name": "Arrangör",
            "desc": "Vårbalsarrnagörerna, som det låter, arrangerar vårbalen, sektionens stora finsittning under våren. Det innebär att de planerar, bestämmer tema, rekryterar underansvariga och jobbare och har en överblick och leder arbetet för att se till att sektionen får en lyckad vårbal.",
            "src": "varbal-arrangor",
            "amount": 3,
            "questions": []
        }]
    },
    {
        "name": "Revisor",
        "src": "#",
        "id": 12,
        "subcategories": [{
            "name": "Revisor",
            "desc": "Revisorerna ska ha koll på sektionens styrdokument och granska och stötta styrelsen och resten av sektionen i deras arbete kring det. Eftersom de ska vara granskande av sektionens arbete är revisorer ofta alumner som inte längre har en särskilt stark koppling till resten av sektionens funktionärer och arbete.",
            "src": "revisor-revisor",
            "amount": 2,
            "questions": []
        }]
    }
]

candidates, categories = read_data(prelim_categories)

