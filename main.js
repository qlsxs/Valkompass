

function generateQuestion(n){
    let container = document.getElementById("compass"); 
    killChildren(container);
    let alternatives = [];
    for(let i = 0; i < choices.length; i++){
        if(choices[i]["questionId"] === n){
            alternatives.push(choices[i]);
        }   
    }
    let questionTitle = document.createElement("h1");
    questionTitle.innerHTML = questions[n]["text"];
    container.append(questionTitle);
    for(let i = 0; i < alternatives.length; i++){
        let answer = document.createElement("button");
        answer.innerHTML = alternatives[i]["text"];
        answer.value = alternatives[i]["candidates"] + "-" + n;
        container.append(answer);
    }
    let nextQ = document.createElement("button");
    nextQ.innerHTML = "Nästa fråga";
    
}

function killChildren(elem){
    // I thought this would be a funny name
    // Removes every child to an element
    elem.innerHTML = "";
}

list = [
    {
        name: "Styret",
        src: "/#"
    },
    {
        name: "Mottagningen",
        src: "/#"
    },
    {
        name: "fkm*",
        src: "/#"
    },
    {
        name: "FSN",
        src: "/#"
    },
    {
        name: "Fysikalen",
        src: "/#"
    },
    {
        name: "FAN",
        src: "/#"
    },
    {
        name: "JämN",
        src: "/#"
    },
    {
        name: "FRum",
        src: "/#"
    },
    {
        name: "FINT",
        src: "/#"
    },
    {
        name: "Fcom",
        src: "/#"
    },
    {
        name: "FN",
        src: "/#"
    },
    {
        name: "Vårbalen",
        src: "/#"
    },
    {
        name: "Revisor",
        src: "/#"
    }
    

]

function createOptionMenu(data){
    let options = []
    // Add all relevant options to display to the list
    for(let i = 0; i < data.length; i++){
        options.push(list[i])
        if(data[i] == 1){
            let opts = subCategories[i];
            for(let j = 0; j < opts.length;j++){
                options.push(opts[j]);
            }
        }
    }
    let id = 0
    let elem = document.getElementById("categoriesList")
    killChildren(elem)
    for(let i = 0; i < options.length; i++){
        let option = document.createElement("div");
        option.classList.add("category");
        option.innerHTML = options[i]["name"];
        if(options[i]["src"] == "/#"){
            console.log(id);
            id++;
        }
        elem.append(option)
    }


}