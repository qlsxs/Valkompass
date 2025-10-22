data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] // Keeps track of which suboptions are open (1 if open, 0 if close)
$(document).ready(() => {
    createOptionMenu([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
})

function generateQuestion(n) {
    let container = document.getElementById("compass");
    killChildren(container);
    let alternatives = [];
    for (let i = 0; i < choices.length; i++) {
        if (choices[i]["questionId"] === n) {
            alternatives.push(choices[i]);
        }
    }
    let questionTitle = document.createElement("h1");
    questionTitle.innerHTML = questions[n]["text"];
    container.append(questionTitle);
    for (let i = 0; i < alternatives.length; i++) {
        let answer = document.createElement("button");
        answer.innerHTML = alternatives[i]["text"];
        answer.value = alternatives[i]["candidates"] + "-" + n;
        container.append(answer);
    }
    let nextQ = document.createElement("button");
    nextQ.innerHTML = "Nästa fråga";

}

function killChildren(elem) {
    // I thought this would be a funny name
    // Removes every child to an element
    elem.innerHTML = "";
}

function hideAllMainChildren() {
    let children = [].slice.call(document.getElementById("main").children)
    for (let i = 0; i < children.length; i++) {
        children[i].style.display = "none";
    }
}

function toggleData(id) {
    console.log(id)
    if (id >= 0 && id < data.length) {
        data[id] = 1 - data[id];
    }
    createOptionMenu(data);
}

function createOptionMenu(data) {
    let options = []
    // Add all relevant options to display to the list
    for (let i = 0; i < data.length; i++) {
        options.push(categories[i])
        if (data[i] == 1) {
            let opts = subCategories[i];
            for (let j = 0; j < opts.length; j++) {
                options.push({ "name": opts[j]["name"], "src": i + "-" + j });
            }
        }
    }
    let elem = document.getElementById("categoriesList")
    killChildren(elem)
    for (let i = 0; i < options.length; i++) {
        // Add all options to display
        let option = document.createElement("div");
        option.classList.add("category");
        option.innerHTML = options[i]["name"];
        if (options[i]["src"] !== "#") {
            option.classList.add("subcategory")
            option.addEventListener("click", function () {
                let info = options[i]["src"].split("-")
                console.log(info)
                openSubcategory(info[0], info[1])
            })
        }
        elem.append(option)
    }
    let children = [].slice.call(elem.children)
    for (let i = children.length - 1; i >= 0; i--) {
        if (children[i].classList.contains("subcategory")) {
            children.splice(i, 1)
        }
    }
    for (let i = 0; i < children.length; i++) {
        children[i].addEventListener("click", function () {
            toggleData(i);
        })
    }
}

function openSubcategory(i, j) {
    // Displays the main menu for subcategory j to category i
    hideAllMainChildren()
    let cat = subCategories[i][j];
    document.getElementById("subcategory-main-menu").style.display = "";
    document.getElementById("subcategory-title").innerHTML = cat["name"];
    document.getElementById("subcategory-description").innerHTML = cat["desc"];
    let subCandidates = candidates[i][j];
    let candidateList = document.getElementById("candidate-list");
    killChildren(candidateList);
    console.log(subCandidates)
    for(let k = 0; k < subCandidates.length; k++){
        let div  = document.createElement("div");
        let img = document.createElement("img")
        let name = document.createElement('p');
        name.innerHTML = subCandidates[k]["name"];
        img.src = "../images/" + subCandidates[k]["pfp"];
        img.classList.add("pfp")
        img.style.width = "60px";
        img.style.height = "60px";
        img.style.marginRight = "15px";
        div.classList.add("candidate-list-div")
        name.classList.add("whiteBtnText");
        name.style.color = "white";
        div.append(img)
        div.append(name);
        candidateList.append(div);
    }

}