from flask import Flask,request,redirect,jsonify,render_template

app = Flask(__name__)

@app.route("/query/", methods=["POST", "GET"])
def query():
    return request.form.get("url", "NO URL :(")

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":          
    app.run(debug=True)