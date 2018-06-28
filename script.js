var textArea = document.getElementById("textArea");
var errorArea = document.getElementById("errorArea");

var sub = new XMLHttpRequest;
sub.onload = function () {
    console.log("should've written");
}

var seeSubs = new XMLHttpRequest;
seeSubs.onload = function () {
    console.log("finished loading submissions. should display now");
    displaySubmissions();
}

function displaySubmit() {

    console.log("clicked \"Submit Kudos\"")
    textArea.innerHTML = "";
    errorArea.innerHTML = "";
    textArea.innerHTML = '<div class="row"><div class="col"><form name="submissionForm"><div class="form-group"><label for="toWho">Kudos to...</label><input autocomplete="off" type="text" class="form-control" id="toWho" name="toWho" placeholder="Enter name"></div><div class="form-group"><label for="whatItSays">for...</label><input autocomplete="off" type="text" class="form-control" placeholder="For Why?" name="whatItSays" id="whatItSays"></div><button type="button" class="btn btn-lg btn-success btn-block" onclick="submitKudos(this.form);">Submit</button></form></div></div>';

}

function loadSubmissions() {

    console.log("clicked \"View Kudos\"");
    textArea.innerHTML = "";
    errorArea.innerHTML = "";
    console.log("starting to load submissions");
    seeSubs.open("GET", "http://homer.stuy.edu/~jchirinos/Kudos/submit.py?sort=none");
    seeSubs.send();
    textArea.innerHTML = '<div class="row"><div class="col text-center">Loading...</div></div>';
}

function displaySubmissions() {
    console.log("displaying submittions:");
    console.log(seeSubs.responseText);
    textArea.innerHTML = seeSubs.responseText;
}

function submitKudos(form) {

    console.log("clicked \"Submit\"");
    errorArea.innerHTML = "";
    var toWho = form.toWho.value;
    var whatItSays = form.whatItSays.value;
    /*if either field is not complete*/
    if (toWho == "" || whatItSays == "") {
        errorArea.innerHTML = "Please fill out both fields";
    }
    /*else submit form */
    else {
        console.log("http://homer.stuy.edu/~jchirinos/Kudos/submit.py?toWho=" + encodeURIComponent(toWho) + "&whatItSays=" + encodeURIComponent(whatItSays));
        sub.open("GET", "http://homer.stuy.edu/~jchirinos/Kudos/submit.py?toWho=" + encodeURIComponent(toWho) + "&whatItSays=" + encodeURIComponent(whatItSays));
        sub.send();
        textArea.innerHTML = "Thank!!!";

    }

}
