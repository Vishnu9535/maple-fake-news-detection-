from flask import Flask, request, redirect, jsonify, render_template, jsonify
import requests as rq
from bs4 import BeautifulSoup

try:
    from core import validate
except:
    from maple.core import validate

app = Flask(__name__)


@app.route("/query/", methods=["POST", "GET"])
def query():

    print(request.form)
    url = request.form.get("URL", "").strip()

    if not url:
        return jsonify({"type": "error"})

    # return jsonify({"type": "response", "URL": url, "valid": True})

    title = BeautifulSoup(rq.get(url).text, "html.parser").find('h1')

    return jsonify({"type": "response", "URL": url, "valid": bool(validate(title.text))})


@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
