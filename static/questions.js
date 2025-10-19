questions = [
    {
        text: "Fråga 1",
        index: 0
    },
    {
        text: "Fråga 2",
        index: 1
    }
]

choices = [
    {
        text: "Bla bla bla",
        candidates: "AB",
        questionId: 0
    },
    {
        text: "Bla bla bla 2",
        candidates: "BC",
        questionId: 0
    },
    {
        text: "Bla bla bla 3",
        candidates: "AD",
        questionId: 0
    },
    {
        text: "Bla bla bla",
        candidates: "AB",
        questionId: 1
    },
    {
        text: "Bla bla bla 2",
        candidates: "AD",
        questionId: 1
    },
    {
        text: "Bla bla bla 3",
        candidates: "CD",
        questionId: 1
    },

]

categories = [
    {
        name: "Styret",
        src: "#"
    },
    {
        name: "Mottagningen",
        src: "#"
    },
    {
        name: "fkm*",
        src: "#"
    },
    {
        name: "FSN",
        src: "#"
    },
    {
        name: "Fysikalen",
        src: "#"
    },
    {
        name: "FAN",
        src: "#"
    },
    {
        name: "JämN",
        src: "#"
    },
    {
        name: "FRum",
        src: "#"
    },
    {
        name: "FINT",
        src: "#"
    },
    {
        name: "Fcom",
        src: "#"
    },
    {
        name: "FN",
        src: "#"
    },
    {
        name: "Vårbalen",
        src: "#"
    },
    {
        name: "Revisor",
        src: "#"
    }


]

subCategories = [
    [ // Styret
        {
            name: "Sektionsordförande",
            desc: "Ordförande har det övergripande ansvaret för sektionen och är ansiktet utåt mot THS och andra sektioner. Ordförande leder också styrelsens arbete under året",
            amount: 1,
        },
        {
            name: "Viceordförande",
            desc: "Vice ordförande stöttar ordförande i att leda sektionen och tar över om hen inte kan utföra sina uppgifter. Vice ordförande har också en mer administrativ roll som bl.a. innebär att hen sammankallar till möten mellan alla nämnder och har hand om sektionens drive.",
            amount: 1,
        },
        {
            name: "Sektionskassör",
            desc: "Sektionens kassör är ytterst ansvarig för sektionens ekonomi. Det innebär att hen ansvarar för sektionens budget och stöttar nämnderna i ekonomiska beslut samt bokför alla utgifter och intäkter sektionen som stort har.",
            amount: 1,
        },
        {
            name: "SSO / Skyddsombud",
            desc: "SSO är en ledamot med extra ansvar för studiesociala och JML-frågor. Det innebär att hen ska se till att alla är trygga och mår bra på sektionen. Hen ska också vara den person sektionens medlemmar kan komma till och prata om det är något och har därför också tystnadsplikt.",
            amount: 1,
        },
        {
            name: "Styrelseledamot",
            desc: "Styrelsen har utöver ordförande, vice, kassör och SSO också tre ledamöter som har ansvar för allmänt styrelsearbete och internt fördelar rollerna eventansvarig, näringslivsansvarig, sekreterare och vice kassör. De driver också ofta egna projekt.",
            amount: 3,
        }
    ],
    [ // Mottagningen
        {
            name: "Fadderist",
            desc: "Fadderisterna är ansvariga för att arrangera sektionens mottagning, de två veckorna i augusti då vi välkomnar alla nyantagna. De har också en teatral roll under mottagningen där de är lite roliga och spexiga.",
            amount: 4,
        }
    ],
    [ //*fkm
        {
            name: "Klubbmästare",
            desc: "Klubbmästarna är ordförande, vice och kassör för klubbmästeriet fkm*. Det innebär att de ansvarar för att arrangera regelbundna pubar och sittningar och ansvarar för all alkoholförsäljning i konsulatet. De rekryterar och leder också alla underansvariga i fkm* som har hand om dekor, mat, märken och dryck på pubar och gasquer.",
            amount: 3,
        }
    ],
    [ //FSN
        {
            name: "SNO",
            desc: "SNO är ordförande för för studienämnden FSN. Hen sköter det administrativa arbetet i studienämnden och representerar sektionens studenter och deras åsikter mot KTH. SNO fixar också event för studienämnden och har en överblick över deras arbete.",
            amount: 1,
        },
        {
            name: "F-PAS",
            desc: "F-PAS är programansvarig student för teknisk fysik och ansvarar därför för kontakt mellan fysikstudenterna och programledningen och examinatorerna när det kommer till studiefrågor. Hen ser till att fysikstudenternas röst hörs när programmet utvecklas.",
            amount: 1,
        },
        {
            name: "TM-PAS",
            desc: "TM-PAS är programansvarig student för teknisk matematik och ansvarar därför för kontakt mellan mattestudenterna och programledningen och examinatorerna när det kommer till studiefrågor. Hen ser också till att mattestudenternas röst hörs när programmet utvecklas. ",
            amount: 1,
        }
    ],
    [ //Fysikalen
        {
            name: "Stabsledningen",
            desc: "Stabsledningen är ordförande, vice och kassör för Fysikalen, sektionens så kallade spex (studentikosa musikalteater). De har ansvar för att rekrytera alla gruppchefer som tillsammans leder och skapar spexet. De väljs vartannat år och sitter i två år.",
            amount: 3,
        }
    ],
    [ //FAN
        {
            name: "Ordförande",
            desc: "Ordförande för aktivitetsnämnden (oFAN) ansvarar för att leda FAN i sitt arbete genom att bl.a. rekrytera underansvariga som fixar små regelbundna aktiviteter och fixa större event som t.ex.  Åreresan och PAFF.",
            amount: 1,
        }
    ],
    [ //JämN
        {
            name: "Ordförande",
            desc: "Jämlikhetsnämndens ordförande (oJämN) är delvis ansvarig för jämlikhetsarbetet på sektionen och leder jämlikhetsnämndens arbete genom att bl.a. rekrytera underansvariga, hålla lunchmöten och planera aktiviteter som har med jämlikhet att göra.",
            amount: 1,
        }
    ],
    [ //FRum
        {
            name: "GK (Ordförande)",
            desc: "GK (Generalkonsul) är ordförande för lokalnämnden FRum. Hen är ansvarig för vår sektionslokal konsulatet och leder tillsammans med CdA FRums arbete genom bl.a. lunchmöten, städdagar och internevent. De rekryterar också underansvariga som bl.a. har ansvar för sektionsbilen.",
            amount: 1,
        },
        {
            name: "CDA (Kassör)",
            desc: "CdA (Chargé d’Affaires) är kassör för lokalnämnden FRum och ansvarig för godisskåpet i konsulatet. Hen leder tillsammans med GK FRums arbete genom bl.a. lunchmöten, städdagar och internevent. De rekryterar också underansvariga som bl.a. har ansvar för sektionsbilen.",
            amount: 1,
        }
    ],
    [ //FINT
        {
            name: "President",
            desc: "FINTo is the head of the international organization in the chapter. They organize meetings, keep in contact with the administration and lead FINT in its day to day work. They are also responsible for the international reception for all exchange students coming to the physics chapter. ",
            amount: 0,
        }
    ],
    [ //Fcom
        {
            name: "Ordförande",
            desc: "Fcoms ordförande ansvarar för att samordna Fcom och dess delnämnder, The Force, F.Dev och FArt som tillsammans har hand om sektionens kommunikation och informationsspridning. Hen är också ansvarig för generella sektionsmärken, ovverallerna och sångboken.",
            amount: 1,
        },
        {
            name: "Webmaster",
            desc: "Webmaster är ansvarig för programmeringsgruppen F.Dev som har programmeringsmöten där de ibland jobbar på olika projekt åt resten av sektionen. Webmaster är också ansvarig för sektionens webbplats.",
            amount: 1,
        },
        {
            name: "Redaktör",
            desc: "Redaktören är ansvarig för sektionstidningen The Force. Hen har hand om att strukturera och publicera tidningen och göra den underhållande både för de som gör den och de som läser.",
            amount: 1,
        },
        {
            name: "Designansvarig",
            desc: "Designansvarig är ansvarig för designgruppen FArt som fixar märken och annan grafik och grafisk profil till resten av sektionen.",
            amount: 1,
        },
    ],
    [ //FN
        {
            name: "Ordförande",
            desc: "Generalsekreteraren är ordförande för näringslivsnämnden FN och leder deras allmänna arbete genom att bl.a. hålla möten, rekrytera underansvariga och ansvarar för annan operativ verksamhet.",
            amount: 1,
        },
        {
            name: "Kassör",
            desc: "FNs kassör är ansvarig för näringslivsnämnden FNs ekonomi och har därför hand om deras budget och ser till att allt bokförs och dokumenteras rätt. FN är en av sektionens större inkomstkällor så det är ett stort ansvar. Hen hjälper också FNs ordförande i att leda nämnden.",
            amount: 1,
        },
        {
            name: "Portföljförvaltare",
            desc: "Portföljförvaltaren ansvarar för sektionens kapitalförvaltning (aktiefond) och leder gruppen F.Cap i att bestämma vilka investeringar som ska göras och inte.",
            amount: 1,
        },
        {
            name: "Fusionsreaktor",
            desc: "Fusionsreaktorn är samordnare och arrangör för fysiksektionens arbetsmarknadsmässa FUSION. Det innebär att de rekryterar underansvariga och har en överblick under arbetet med att skapa mässan.",
            amount: 1,
        }
    ],
    [ //Vårbalen
        {
            name: "Arrangör",
            desc: "Vårbalsarrnagörerna, som det låter, arrangerar vårbalen, sektionens stora finsittning under våren. Det innebär att de planerar, bestämmer tema, rekryterar underansvariga och jobbare och har en överblick och leder arbetet för att se till att sektionen får en lyckad vårbal.",
            amount: 3,
        }
    ],
    [ //Revisor
        {
            name: "SPECIAL",
            desc: "Revisorerna ska ha koll på sektionens styrdokument och granska och stötta styrelsen och resten av sektionen i deras arbete kring det. Eftersom de ska vara granskande av sektionens arbete är revisorer ofta alumner som inte längre har en särskilt stark koppling till resten av sektionens funktionärer och arbete.",
            amount: 2,
        }
    ],

]

candidates = [
    [ // Styret
        [
            {
                "name": "Förnamn Efternamn 1",
                "year": 22,
                "qna": [],
                "pfp": "image.png"
            },
            {
                "name": "Förnamn Efternamn 2",
                "year": 20,
                "qna": [],
                "pfp": "image2.jpg"
            },
            {
                "name": "Förnamn Efternamn 3",
                "year": 25,
                "qna": [],
                "pfp": "image3.png"
            }
        ], [

        ], [

        ], [

        ], [

        ]
    ],
    [ // Mottagningen
        [

        ]
    ],
    [ //*fkm
        []
    ],
    [ //FSN
        [], [], []
    ],
    [ //Fysikalen
        []
    ],
    [ //FAN
        []
    ],
    [ //JämN
        []
    ],
    [ //FRum
        [], []
    ],
    [ //FINT
        []
    ],
    [ //Fcom
        [], [], [], []
    ],
    [ //FN
        [], [], [], []
    ],
    [ //Vårbalen
        []
    ],
    [ //Revisor
        []
    ],

]


