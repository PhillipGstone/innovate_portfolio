
function changeText(id) {
    id.innerHTML = "you have changed this text with an 'onclick' event"
}

function displayDate(id) {
    document.getElementById("date").innerHTML = Date();
}

// function checkCookies() {
//     let text = ""
//     if (navigator.cookiesEnabled == true) {
//         text = "cookies are enabled";
//     } else {
//         text = "cookies are not enabled";
//     }
//     document.getElementById("cookie").innerHTML = text;
// }

function mOver(obj) {
    obj.innerHTML = "<br> HELLO"
}

function mOut(obj) {
    obj.innerHTML = ""
}

function sendAlert() {
    alert(location.hostname);
}

function darkmodetoggle() {
    let element = document.body;  // Variable . Looking at the base and picking body.
    let mainbox = document.getElementsByClassName("main-box");
    let mainText = document.getElementsByClassName("main-text");
    let state = localStorage.getItem("state");

    element.classList.toggle("dark-mode"); // using Veribale then toggle what we called it on .html page. Don't forget to link it tho.

    for (const box of mainbox) {
        box.classList.toggle("dark-mode-b");  
    }

    for (const text of mainText) {
        text.classList.toggle("dark-mode-b");
    }

    if (state !=="dark") {
        localStorage.setItem("state", "dark"); 
    } else {
        localStorage.setItem("state", "light"); 
    }
}


function darkCheck() {
    let element = document.body;  
    let mainbox = document.getElementsByClassName("main-box");
    let mainText = document.getElementsByClassName("main-text");
    let state = localStorage.getItem("state")

    if (state =="dark") {
        element.classList.toggle("dark-mode");  
    

        for (const box of mainbox) {
            box.classList.toggle("dark-mode-b");  
        }
    
        for (const text of mainText) {
            text.classList.toggle("dark-mode-b");
        }
    }
    let text = ""
    if (navigator.cookiesEnabled == true) {
        text = "cookies are enabled";
    } else {
        text = "cookies are not enabled";
    }
    document.getElementById("cookie").innerHTML = text;
}

text = "Once more unto something, something..." 
function diffText() {
    document.getElementById("word_guy").innerHTML = text;
    }
