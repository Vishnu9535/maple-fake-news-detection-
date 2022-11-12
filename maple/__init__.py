from flask import Flask, request, redirect, jsonify, render_template, jsonify
import requests as rq
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/query/", methods=["POST", "GET"])
def query():
    url = request.form.get("URL", None)

    if not url:
        return jsonify({"type": "error"})

    title = BeautifulSoup(rq.get(url).text, "html.parser").find('h1').text

    result = validate(title)

    return jsonify({"URL": url, "valid": result})

    # if request.method == "POST":
    #     pass

    # else:
    #     return "GET not supported."


@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
