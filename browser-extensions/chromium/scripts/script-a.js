

function _maple_validateURL(u) {
    var fd = new FormData();
    fd.append("URL", u)

    fetch("http://localhost:5000/query/", {
        method: "POST",
        body: fd
    }).then(resp => resp.json()).then(resp => {
        console.log(resp);
    })
}


function validate_article(u) {
    var xr = new XMLHttpRequest();
    xr.open("POST", "http://localhost:5000/query/")

    xr.send(JSON.stringify({
        "URL": u
    }))

    return xr
}


function make_maple() {
    const mp = document.createElement("div");
}




window.onload = () => {
    var u = document.URL;

    var x = validate_article(u);
    x.addEventListener("readystatechange", function () {
        console.log("HERE");
        if (this.readyState === 4) {
            console.log(this.responseText);
        }
    });
}
