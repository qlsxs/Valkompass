function killChildren(elem) {
    // I thought this would be a funny name
    // Removes every child to an element
    elem.innerHTML = "";
}

function toggleShownSubcategories(i) {
    // Puts display none or removes display none on the i:th categories subcategories
    children = [].slice.call(document.getElementById("categoriesList").children)
    let m = 0
    while (m <= i) {
        if (!children[0].classList.contains("subcategory")) {
            m += 1
        }
        children.shift()
    }
    while (children[0].classList.contains("subcategory")) {
        if (children[0].style.display == "none") {
            children[0].style.display = "";
        }
        else {
            children[0].style.display = "none";
        }
        children.shift()
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
    for (let k = 0; k < subCandidates.length; k++) {
        let div = document.createElement("div");
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

function calculateRadioRadius(id) {
    // Returns the width/height of the radio buttons for the questions
    if (document.getElementById(id) != null) {
        const total = document.getElementById(id).offsetWidth;
        return (total - 40) / 11;
    }
}

function selectOption(cat, id, qnr) {
    // This function is called when the user clicks on the radio button for score id on category cat. Reveals the candiate scores and updates individual choice
    // Reveal candidates
    let candidatePlacing = [].slice.call(document.getElementsByClassName("radioCircleImage"))

    for (let i = 0; i < candidatePlacing.length; i++) {
        candidatePlacing[i].style.display = "block";
    }
    // Reset color on other elemnts and color the user picked one.
    // Color the one the user piocked
    let options = [].slice.call(document.getElementsByClassName("radioCircle"))
    for (let i = 0; i < options.length; i++) {
        if (i == id) {
            options[i].style.borderColor = "#FF642B"
            options[i].innerHTML = "Du"
        }
        else {
            options[i].style.borderColor = "white"
            options[i].innerHTML = ""
        }
    }
    document.getElementById("orangeButton").innerHTML = "Nästa"
    updateSessionScore(cat, id, qnr)
}

function updateSessionScore(cat, score, qnr){
    // Stores whatever the user chose as session to display at the summary/if they go back to this page
    $.ajax({
        type: "POST",
        url: "/update_session_score",
        data: JSON.stringify({"cat":cat, "score": score, "question_id":qnr}),
        dataType: "json",
        headers: {
            'Content-Type': 'application/json'
        },
        error: (err) => {
            console.log("Error:" +  err)
        }
    })
}

function revealReason(id) {
    // Creates a speech-bubble like element containing the reason for the person clicked on voting what they voted.
    let circleElem = document.getElementById(id)
    let rect = circleElem.getBoundingClientRect()
    let cont = document.getElementById("subcategory-main-menu")
    let rect2 = cont.getBoundingClientRect()
    let reasonDiv = document.createElement("div")
    let x = (rect.right - rect.left) / 2 + rect.left - rect2.left - 14.14
    let y = rect.bottom
    reasonDiv.id = "speechBubbleReason"
    reasonDiv.style.left = rect2.left + "px"
    reasonDiv.style.width = rect2.right - rect2.left + "px"
    reasonDiv.style.top = y + 16.143 + "px"
    reasonDiv.style.setProperty("--speechBubbleTriangleLeft", x + "px")
    
    let div1 = document.createElement("div")
    let div2 = document.createElement("div")
    div1.style.flexGrow = 3
    div1.style.marginRight = "10px";
    div2.style.flexGrow = 7
    let img = document.createElement('img')
    img.src = document.getElementById(id + "-img").src
    img.id = "speechBubbleReasonImage"
    let info = document.createElement('p')
    info.classList.add("bodyText")
    info.innerHTML = "<strong>" + document.getElementById(id + "-name").innerHTML +"</strong><br>" +  document.getElementById(id + "-reason").innerHTML
    info.style.flexGrow = 1
    info.style.color = "white"
    div1.append(img)
    div2.append(info)
    reasonDiv.append(div1)
    reasonDiv.append(div2)
    document.body.append(reasonDiv)
    reasonDiv.height = info.offsetHeight + "px"
    setTimeout(() => $(document).one('click', ((e) => { removeReasonMenu(e) })), 10)
}

function removeReasonMenu(e) {
    const menu = document.getElementById("speechBubbleReason")
    const closest = e.target.closest("div")
    if (menu !== null && closest == null || closest.id !== "speechBubbleReason") {
        menu.remove()
    }
    else {
        setTimeout(() => $(document).one('click', ((e) => { removeReasonMenu(e) })), 10)
    }
}

function toggleVisibility(id){
    let elem = document.getElementById(id)
    if(elem.style.display === "none"){
        elem.style.display = ""
    }
    else{
        elem.style.display = "none"
    }
}

