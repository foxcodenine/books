//JS code goes here
// _____________________________________________________________________
// Elements 
let textbox = document.querySelector("#input-text");
let regexbox = document.querySelector("#input-regex");
let alertbox = document.querySelector("#alert-box");
let resultsbox = document.querySelector("#results-box");
let testButton = document.querySelector("#test-button");

// _____________________________________________________________________
// Event Listeners 

testButton.addEventListener('click', () => {
    
    // ----- clear page from previous run

    clearResultAndErrors();

    // ----- get current values

    let text = textbox.value;
    console.log(text);

    let regex = regexbox.value;
    console.log(regex);

    // ----- handle empty values

    if (text.trim() == "") {
        err("Please enter some text to test.");

    } else if (regex.trim() == "") {
        err("Please enter a regular expression.");
    } else {
        regex = createRegex(regex);

        if (!regex) {
            return;
        } 
    }
    // ----- get matches

    let results = getMatches(regex, text);

    if (results.length > 0 && results[0] !== null) {
        let html = getMatchesCountString(results);
        html += getResultsString(results, text);
        resultsbox.innerHTML = html;
    } else {
        resultsbox.textContent = "There were no matches.";
    }
});

// _____________________________________________________________________
// Helper Function 

function clearResultAndErrors() {
    resultsbox.textContent = "";

    alertbox.textContent = "";
    alertbox.classList.add("hide");
}

// __________________

function err(str) {
    alertbox.textContent = str;
    alertbox.classList.remove("hide");
}

// __________________

function createRegex(regex) {
    try {
        if (regex.charAt(0) == "/") {

            // spit in to array
            regex = regex.split("/"); 
            
            // remove 1st item
            regex.shift(); 

            // remove last item and save it to flags
            let flags = regex.pop(); 

            // recreate string
            regex = regex.join("/"); 

            // create regexp
            regex = new RegExp(regex, flags);

        } else {
            regex = new RegExp(regex, "g");
        }
        return regex;

    } catch (e) {
        err("The Regular Expression in invalid.");
        console.log(e);
        return false;
    }
}

// __________________

function getMatches(regex, text) {
    let results = [];
    let result;

    // The global property indicates whether or not the "g" flag is
    // used with the regular expression.

    if (regex.global) {
        while((result = regex.exec(text)) !== null) {
            results.push(result);
        } 
    } else {
        results.push(regex.exec(text));
    }
    return results;  
}

// __________________

function getMatchesCountString(results) {
    if (results.length === 1) {
        return "<p>There was one match.</p>";
    } else {
        return `<p>There are ${results.length} matches.</p>`;
    }
}

// __________________

function getResultsString(results, text) {
    for (var i = results.length - 1; i >= 0; i--) {
        let result = results[i];
        let match  = result.toString();
        let prefix = text.substr(0, result.index)
        let suffix = text.substr(result.index + match.length);

        text = prefix
            + '<span class="label label-info">'
            + match
            + '</span>'
            + suffix;
    }
    return "<h4>" + text + "</h4>";
}
// _____________________________________________________________________