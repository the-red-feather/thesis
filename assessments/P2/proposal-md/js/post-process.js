// NAME:        post-process.js
// DATE:        2021-05-21
// AUTHOR:      Jos Feenstra
// PURPOSE:     an experiment to do semi-LaTeX things with markdown by simply using javascript like you would on a web page 
// NOTES :      I should try and use this: https://www.pagedjs.org/examples/
//              See also this: https://github.com/jaantollander/Markdown-Templates. 
//              It uses something called 'pandoc' to go from markdown -> LaTeX -> Pdf                

function main() {
    setDate(".auto-date");
    setContent("#content");
    setReferences("#references");
    
}


function setContent(contentId) {
    let content = document.querySelector(contentId);
    if (!content) {
        console.error("couldnt find content!")
        return 
    }

    // give everything the correct number
    let id = 1;
    content.querySelector('h1').forEach(h => {
        h.innerText = `${id}. ${h.innerText}`;  
        id++;
    })

}

function setReferences(refId) {

}


/**
 * query selects elements, and fills these elements with 
 * a text representing the current day of the year
 * @param {string} query 
 */
function setDate(query) {

    const MONTH_NAMES = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
    ];

    console.log("lalalal");
    for (let e of document.querySelectorAll(query)) {
        console.log("lalala")
        var dateObj = new Date();
        var month = dateObj.getUTCMonth(); //months from 0-11
        var day = dateObj.getUTCDate();
        var year = dateObj.getUTCFullYear();
        newdate = day + " " + MONTH_NAMES[month] + " " + year;
        e.innerText = newdate;
    }
}

window.addEventListener('load', main);