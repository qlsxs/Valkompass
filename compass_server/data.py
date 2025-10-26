categories = [
    {
        "name": "Styret",
        "src": "#",
        "id": 0
    },
    {
        "name": "Mottagningen",
        "src": "#",
        "id": 1
    },
    {
        "name": "fkm*",
        "src": "#",
        "id": 2
    },
    {
        "name": "FSN",
        "src": "#",
        "id": 3
    },
    {
        "name": "Fysikalen",
        "src": "#",
        "id": 4
    },
    {
        "name": "FAN",
        "src": "#",
        "id": 5
    },
    {
        "name": "JämN",
        "src": "#",
        "id": 6
    },
    {
        "name": "FRum",
        "src": "#",
        "id": 7
    },
    {
        "name": "FINT",
        "src": "#",
        "id": 8
    },
    {
        "name": "Fcom",
        "src": "#",
        "id": 9
    },
    {
        "name": "FN",
        "src": "#",
        "id": 10
    },
    {
        "name": "Vårbalen",
        "src": "#",
        "id": 11
    },
    {
        "name": "Revisor",
        "src": "#",
        "id": 12
    }


]

subCategories = [
    [  # Styret
        {
            "name": "Sektionsordförande",
            "desc": "Ordförande har det övergripande ansvaret för sektionen och är ansiktet utåt mot THS och andra sektioner. Ordförande leder också styrelsens arbete under året.",
            "src": "styret-ordforande",
            "amount": 1,
            "candidates": [
                {
                    "name": "Förnamn Efternamn 1",
                    "year": 22,
                    "pfp": "image.png",
                    "answers": [{"value": 3, "reason": "bla bbla bla"}, {"value": 1, "reason": "badsfla bbla bla"}, {"value": 5, "reason": "bla bbla asdfbla"}]
                },
                {
                    "name": "Förnamn Efternamn 2",
                    "year": 20,
                    "pfp": "image2.jpg",
                    "answers": [{"value": 5, "reason": "bla bbasfdasdfla bla"}, {"value": 4, "reason": "badsflasdfa bbla bla"}, {"value": 9, "reason": "bla basdfbla asdfbla"}]
                },
                {
                    "name": "Förnamn Efternamn 3",
                    "year": 25,
                    "pfp": "image3.png",
                    "answers": [{"value": 3, "reason": "bla bbldfssdfa bla"}, {"value": 3, "reason": "badsfla bbla bla"}, {"value": 6, "reason": "bla bbsadfsadf fasdfsadfsd asadffsdsfdla asdfbla"}]
                }
            ],
            "questions": [
                "fråga fråga fråga1", "frågafråga fråga2", "fråga fråga fråga 3"
            ]
        },
        {
            "name": "Viceordförande",
            "desc": "Vice ordförande stöttar ordförande i att leda sektionen och tar över om hen inte kan utföra sina uppgifter. Vice ordförande har också en mer administrativ roll som bl.a. innebär att hen sammankallar till möten mellan alla nämnder och har hand om sektionens drive.",
            "src": "styret-viceordforande",
            "amount": 1,
        },
        {
            "name": "Sektionskassör",
            "desc": "Sektionens kassör är ytterst ansvarig för sektionens ekonomi. Det innebär att hen ansvarar för sektionens budget och stöttar nämnderna i ekonomiska beslut samt bokför alla utgifter och intäkter sektionen som stort har.",
            "src": "styret-kassor",
            "amount": 1,
        },
        {
            "name": "SSO / Skyddsombud",
            "desc": "SSO är en ledamot med extra ansvar för studiesociala och JML-frågor. Det innebär att hen ska se till att alla är trygga och mår bra på sektionen. Hen ska också vara den person sektionens medlemmar kan komma till och prata om det är något och har därför också tystnadsplikt.",
            "src": "styret-sso",
            "amount": 1,
        },
        {
            "name": "Styrelseledamot",
            "desc": "Styrelsen har utöver ordförande, vice, kassör och SSO också tre ledamöter som har ansvar för allmänt styrelsearbete och internt fördelar rollerna eventansvarig, näringslivsansvarig, sekreterare och vice kassör. De driver också ofta egna projekt.",
            "src": "styret-ledamot",
            "amount": 3,
        }
    ],
    [  # Mottagningen
        {
            "name": "Fadderist",
            "desc": "Fadderisterna är ansvariga för att arrangera sektionens mottagning, de två veckorna i augusti då vi välkomnar alla nyantagna. De har också en teatral roll under mottagningen där de är lite roliga och spexiga.",
            "src": "mottagningen-fadderist",
            "amount": 4,
        }
    ],
    [  # *fkm
        {
            "name": "Klubbmästare",
            "desc": "Klubbmästarna är ordförande, vice och kassör för klubbmästeriet fkm*. Det innebär att de ansvarar för att arrangera regelbundna pubar och sittningar och ansvarar för all alkoholförsäljning i konsulatet. De rekryterar och leder också alla underansvariga i fkm* som har hand om dekor, mat, märken och dryck på pubar och gasquer.",
            "src": "fkm-klubbmastare",
            "amount": 3,
        }
    ],
    [  # FSN
        {
            "name": "SNO",
            "desc": "SNO är ordförande för för studienämnden FSN. Hen sköter det administrativa arbetet i studienämnden och representerar sektionens studenter och deras åsikter mot KTH. SNO fixar också event för studienämnden och har en överblick över deras arbete.",
            "src": "fsn-sno",
            "amount": 1,
        },
        {
            "name": "F-PAS",
            "desc": "F-PAS är programansvarig student för teknisk fysik och ansvarar därför för kontakt mellan fysikstudenterna och programledningen och examinatorerna när det kommer till studiefrågor. Hen ser till att fysikstudenternas röst hörs när programmet utvecklas.",
            "src": "fsn-fpas",
            "amount": 1,
        },
        {
            "name": "TM-PAS",
            "desc": "TM-PAS är programansvarig student för teknisk matematik och ansvarar därför för kontakt mellan mattestudenterna och programledningen och examinatorerna när det kommer till studiefrågor. Hen ser också till att mattestudenternas röst hörs när programmet utvecklas. ",
            "src": "fsn-tmpas",
            "amount": 1,
        }
    ],
    [  # Fysikalen
        {
            "name": "Stabsledningen",
            "desc": "Stabsledningen är ordförande, vice och kassör för Fysikalen, sektionens så kallade spex (studentikosa musikalteater). De har ansvar för att rekrytera alla gruppchefer som tillsammans leder och skapar spexet. De väljs vartannat år och sitter i två år.",
            "src": "fysikalen-stabsledning",
            "amount": 3,
        }
    ],
    [  # FAN
        {
            "name": "Ordförande",
            "desc": "Ordförande för aktivitetsnämnden (oFAN) ansvarar för att leda FAN i sitt arbete genom att bl.a. rekrytera underansvariga som fixar små regelbundna aktiviteter och fixa större event som t.ex.  Åreresan och PAFF.",
            "src": "fan-ordforande",
            "amount": 1,
        }
    ],
    [  # JämN
        {
            "name": "Ordförande",
            "desc": "Jämlikhetsnämndens ordförande (oJämN) är delvis ansvarig för jämlikhetsarbetet på sektionen och leder jämlikhetsnämndens arbete genom att bl.a. rekrytera underansvariga, hålla lunchmöten och planera aktiviteter som har med jämlikhet att göra.",
            "src": "jamn-ojamn",
            "amount": 1,
        }
    ],
    [  # FRum
        {
            "name": "GK (Ordförande)",
            "desc": "GK (Generalkonsul) är ordförande för lokalnämnden FRum. Hen är ansvarig för vår sektionslokal konsulatet och leder tillsammans med CdA FRums arbete genom bl.a. lunchmöten, städdagar och internevent. De rekryterar också underansvariga som bl.a. har ansvar för sektionsbilen.",
            "src": "frum-gk",
            "amount": 1,
        },
        {
            "name": "CDA (Kassör)",
            "desc": "CdA (Chargé d’Affaires) är kassör för lokalnämnden FRum och ansvarig för godisskåpet i konsulatet. Hen leder tillsammans med GK FRums arbete genom bl.a. lunchmöten, städdagar och internevent. De rekryterar också underansvariga som bl.a. har ansvar för sektionsbilen.",
            "src": "frum-cda",
            "amount": 1,
        }
    ],
    [  # FINT
        {
            "name": "President",
            "desc": "FINTo is the head of the international organization in the chapter. They organize meetings, keep in contact with the administration and lead FINT in its day to day work. They are also responsible for the international reception for all exchange students coming to the physics chapter. ",
            "src": "fint-president",
            "amount": 0,
        }
    ],
    [  # Fcom
        {
            "name": "Ordförande",
            "desc": "Fcoms ordförande ansvarar för att samordna Fcom och dess delnämnder, The Force, F.Dev och FArt som tillsammans har hand om sektionens kommunikation och informationsspridning. Hen är också ansvarig för generella sektionsmärken, ovverallerna och sångboken.",
            "src": "fcom-ordforande",
            "amount": 1,
        },
        {
            "name": "Webmaster",
            "desc": "Webmaster är ansvarig för programmeringsgruppen F.Dev som har programmeringsmöten där de ibland jobbar på olika projekt åt resten av sektionen. Webmaster är också ansvarig för sektionens webbplats.",
            "src": "fcom-webmaster",
            "amount": 1,
        },
        {
            "name": "Redaktör",
            "desc": "Redaktören är ansvarig för sektionstidningen The Force. Hen har hand om att strukturera och publicera tidningen och göra den underhållande både för de som gör den och de som läser.",
            "src": "fcom-redaktor",
            "amount": 1,
        },
        {
            "name": "Designansvarig",
            "desc": "Designansvarig är ansvarig för designgruppen FArt som fixar märken och annan grafik och grafisk profil till resten av sektionen.",
            "src": "fcom-design",
            "amount": 1,
        },
    ],
    [  # FN
        {
            "name": "Ordförande",
            "desc": "Generalsekreteraren är ordförande för näringslivsnämnden FN och leder deras allmänna arbete genom att bl.a. hålla möten, rekrytera underansvariga och ansvarar för annan operativ verksamhet.",
            "src": "fn-ordforande",
            "amount": 1,
        },
        {
            "name": "Kassör",
            "desc": "FNs kassör är ansvarig för näringslivsnämnden FNs ekonomi och har därför hand om deras budget och ser till att allt bokförs och dokumenteras rätt. FN är en av sektionens större inkomstkällor så det är ett stort ansvar. Hen hjälper också FNs ordförande i att leda nämnden.",
            "src": "fn-kassor",
            "amount": 1,
        },
        {
            "name": "Portföljförvaltare",
            "desc": "Portföljförvaltaren ansvarar för sektionens kapitalförvaltning (aktiefond) och leder gruppen F.Cap i att bestämma vilka investeringar som ska göras och inte.",
            "src": "fn-portsfoljforvaltare",
            "amount": 1,
        },
        {
            "name": "Fusionsreaktor",
            "desc": "Fusionsreaktorn är samordnare och arrangör för fysiksektionens arbetsmarknadsmässa FUSION. Det innebär att de rekryterar underansvariga och har en överblick under arbetet med att skapa mässan.",
            "src": "fn-fusionsreaktor",
            "amount": 1,
        }
    ],
    [  # Vårbalen
        {
            "name": "Arrangör",
            "desc": "Vårbalsarrnagörerna, som det låter, arrangerar vårbalen, sektionens stora finsittning under våren. Det innebär att de planerar, bestämmer tema, rekryterar underansvariga och jobbare och har en överblick och leder arbetet för att se till att sektionen får en lyckad vårbal.",
            "src": "varbal-arrangor",
            "amount": 3,
        }
    ],
    [  # Revisor
        {
            "name": "SPECIAL",
            "desc": "Revisorerna ska ha koll på sektionens styrdokument och granska och stötta styrelsen och resten av sektionen i deras arbete kring det. Eftersom de ska vara granskande av sektionens arbete är revisorer ofta alumner som inte längre har en särskilt stark koppling till resten av sektionens funktionärer och arbete.",
            "src": "revisor-revisor",
            "amount": 2,
        }
    ],

]

candidates = [
    [  # Styret
        [
            {
                "name": "Förnamn Efternamn 1",
                "year": 22,
                "pfp": "image.png"
            },
            {
                "name": "Förnamn Efternamn 2",
                "year": 20,
                "pfp": "image2.jpg"
            },
            {
                "name": "Förnamn Efternamn 3",
                "year": 25,
                "pfp": "image3.png"
            }
        ], [

        ], [

        ], [

        ], [

        ]
    ],
    [  # Mottagningen
        [

        ]
    ],
    [  # *fkm
        []
    ],
    [  # FSN
        [], [], []
    ],
    [  # Fysikalen
        []
    ],
    [  # FAN
        []
    ],
    [  # JämN
        []
    ],
    [  # FRum
        [], []
    ],
    [  # FINT
        []
    ],
    [  # Fcom
        [], [], [], []
    ],
    [  # FN
        [], [], [], []
    ],
    [  # Vårbalen
        []
    ],
    [  # Revisor
        []
    ],
]

questions = [
    [  # Styret
        [
            "fråga fråga fråga1", "frågafråga fråga2", "fråga fråga fråga 3"
        ], [

        ], [

        ], [

        ], [

        ]
    ],
    [  # Mottagningen
        [

        ]
    ],
    [  # *fkm
        []
    ],
    [  # FSN
        [], [], []
    ],
    [  # Fysikalen
        []
    ],
    [  # FAN
        []
    ],
    [  # JämN
        []
    ],
    [  # FRum
        [], []
    ],
    [  # FINT
        []
    ],
    [  # Fcom
        [], [], [], []
    ],
    [  # FN
        [], [], [], []
    ],
    [  # Vårbalen
        []
    ],
    [  # Revisor
        []
    ],
]

candidates_answers = [
    [  # Styret
        [
            [{"value": 1, "reason": "bla bliasdikopiasjk dopasjkdopajsdijasidji asjdisjkdopajsdijasidjiasjdisjkd opajsdijasidjiasjdisjkdo ajsdijasidjiasjdisjkdopa jsdijasidjiasjdis jkdopajsdijasidjiasj disjkdopajsdijasidjiasjd isjkdopajsdijasidjiasjdisj dopajsdijasidjias jdisjkdopajsdijasidjiasjdisjkdopajsdijas idjiasjdisjkdopajsd ijasidjiasjd isjkdopajsdijasi djiasjdis jkdopajsdija sidjiasjdia bla"}, {
                "value": 1, "reason": "bla b1la bla"}, {"value": 3, "reason": "bla b4la bla"}],  # ans to q1
            [{"value": 4, "reason": "bla bla 23bla"}, {"value": 3, "reason": "bla42 bla bla"}, {
                "value": 5, "reason": "bla 134la bla"}],  # ans to q2
            [{"value": 5, "reason": "bla dfsbla bla"}, {"value": 3, "reason": "bla sadfbla bla"}, {
                "value": 5, "reason": "bla blsdfa bla"}]  # ans to q3
        ], [

        ], [

        ], [

        ], [

        ]
    ],
    [  # Mottagningen
        [

        ]
    ],
    [  # *fkm
        []
    ],
    [  # FSN
        [], [], []
    ],
    [  # Fysikalen
        []
    ],
    [  # FAN
        []
    ],
    [  # JämN
        []
    ],
    [  # FRum
        [], []
    ],
    [  # FINT
        []
    ],
    [  # Fcom
        [], [], [], []
    ],
    [  # FN
        [], [], [], []
    ],
    [  # Vårbalen
        []
    ],
    [  # Revisor
        []
    ],
]


def get_all_categories():
    # Returns all categories and subcategories
    cats = []
    for i in range(0, len(categories)):
        cats.append(categories[i])
        for j in range(0, len(subCategories[i])):
            condensed_subcat = {"name": subCategories[i][j]["name"], "src": subCategories[i][j]["src"]}
            cats.append(condensed_subcat)
    return cats



def get_subcategory(cat):
    # Returns the subcategory with src cat
    for i in range(0, len(subCategories)):
        for j in range(0, len(subCategories[i])):
            if (subCategories[i][j]["src"] == cat):
                return subCategories[i][j]
            
def get_data_for_question(cat, i):
    # Returns everything neccesary to display the i:th question for the category cat
    category = get_subcategory(cat)
    if(category == None):
        return None, None, None, None
    candidates = []
    if(i == -1): 
        i = len(category["candidates"])-1
    if(i < 0 or i > len(category["candidates"])):
        return None, None, None, None
    if(i == len(category["candidates"])):
        return "Max", "Max", "Max", "Max"
    for cand in category["candidates"]:
        # only display the data for the relevant question, send less stuff
        candidates.append({"name": cand["name"], "year": cand["year"], "pfp": cand["pfp"], "answer": cand["answers"][i]})
    return {"name": category["name"], "desc": category["desc"], "src":category["src"]}, candidates, category["questions"][i], i
        


def get_question(cat, id):
    for i in range(0, len(subCategories)):
        for j in range(0, len(subCategories[i])):
            if (subCategories[i][j]["src"] == cat):
                if (id == len(questions[i][j])):
                    return "Max"
                elif (id > len(questions[i][j])):
                    return None
                return questions[i][j][id]


def get_candidate_answers_for_question(cat, id):
    for i in range(0, len(subCategories)):
        for j in range(0, len(subCategories[i])):
            if (subCategories[i][j]["src"] == cat):
                return candidates_answers[i][j][id]
