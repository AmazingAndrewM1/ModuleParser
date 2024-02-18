from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder="staticFiles")

@app.route("/")
def index():
    return render_template("Hackathon_2024.html")

if __name__ == "__main__":
    app.run(debug=True)