from flask import Flask, request, redirect, jsonify, render_template, jsonify
import requests as rq
from bs4 import BeautifulSoup

from core import validate

app = Flask(__name__)


@app.route("/query/", methods=["POST", "GET"])
def query():
    url = request.form.get("URL", None).strip()

    if not url:
        return jsonify({"type": "error"})

    title = BeautifulSoup(rq.get(url).text, "html.parser").find('h1').text

    result = validate(title)

    return jsonify({"URL": url, "valid": bool(result)})


@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8012, debug=True)
