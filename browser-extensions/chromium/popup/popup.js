
const bodydom = document.getElementsByTagName("body")[0];
console.log(bodydom);

chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
    var u = tabs[0].url;
    console.log(u);

    var fd = new FormData();
    fd.append("URL", u)

    var x = new XMLHttpRequest();
    x.open("POST", "http://localhost:5000/query/")
    x.send(fd);

    x.addEventListener("readystatechange", function () {
        var v = JSON.parse(this.responseText).valid
        console.log(v);

        if (v == true) {
            bodydom.style.backgroundColor = "lime";
        } else {
            bodydom.style.backgroundColor = "firebrick";
            bodydom.style.color = "white";
        }
    });

})

