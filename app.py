from flask import Flask
from flask import render_template, request
import savy_parser

app = Flask(__name__, static_folder="staticFiles")

@app.route("/")
def index():
    return render_template("Hackathon_2024.html")

@app.route("/logic", methods=["POST"])
def logic():
    if request.method == "POST":
        userInput = request.form["userInput"]
        try:
            parseObject = savy_parser.Parser(userInput)
            print(parseObject.truth_table)
        except (Exception, ValueError) as err:
            print(err)
        return render_template("Hackathon_2024.html")


if __name__ == "__main__":
    app.run(debug=True)