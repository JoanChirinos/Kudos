var textArea = document.getElementById("textArea");
var errorArea = document.getElementById("errorArea");

function displaySubmit() {

    console.log("clicked \"Submit Kudos\"")
    textArea.innerHTML = "";
    errorArea.innerHTML = "";
    textArea.innerHTML = '<form name="submissionForm"><div class="form-group"><label for="toWho">Kudos to...</label><input type="text" class="form-control" id="toWho" name="toWho" placeholder="Enter name"></div><div class="form-group"><label for="whatItSays">for...</label><input type="text" class="form-control" placeholder="For Why?" name="whatItSays" id="whatItSays"></div><button type="button" class="btn btn-lg btn-success btn-block" onclick="submitKudos(this.form);">Submit</button></form>';

}

function displayView() {

    console.log("clicked \"View Kudos\"");
    textArea.innerHTML = "";
    errorArea.innerHTML = "";

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

        var sub = new XMLHttpRequest;
        console.log("http://homer.stuy.edu/~jchirinos/Kudos/submit.py?toWho=" + encodeURIComponent(toWho) + "?whatItSays=" + encodeURIComponent(whatItSays));
        sub.open("GET", "http://homer.stuy.edu/~jchirinos/Kudos/submit.py?toWho=" + encodeURIComponent(toWho) + "&whatItSays=" + encodeURIComponent(whatItSays));
        textArea.innerHTML = "Thank!!!"

    }

}
