function killChildren(elem) {
    // I thought this would be a funny name
    // Removes every child to an element
    elem.innerHTML = "";
}

function toggleShownSubcategories(i){
    // Puts display none or removes display none on the i:th categories subcategories
    children = [].slice.call(document.getElementById("categoriesList").children)
    let m = 0
    while(m <= i){
        if(!children[0].classList.contains("subcategory")){
            m += 1
        }
        children.shift()
    }
    while(children[0].classList.contains("subcategory")){
        if(children[0].style.display == "none"){
            children[0].style.display = "";
        } 
        else{
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