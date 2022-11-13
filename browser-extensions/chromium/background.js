

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.contentScriptQuery == "is-valid") {
        var u = request.url;

        fetch("https://localhost:5000/query/", {
            method: "POST",
            body: JSON.stringify({"URL": u})
        }).then(resp => resp.json()).then(resp => {
            console.log(resp);
            sendResponse(resp);
        });
    }
});
