from flask import Flask, render_template, request
from roadmap import generate_roadmap

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        role = request.form["role"]
        roadmap = generate_roadmap(role)
        return render_template("result.html", role=role, roadmap=roadmap)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
