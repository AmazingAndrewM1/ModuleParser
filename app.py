from flask import Flask
from flask import render_template, request
import savy_parser

# Assuming the Parser class and related classes are defined here or imported

app = Flask(__name__, static_folder="staticFiles")


@app.route("/")
def index():
    return render_template("Hackathon_2024.html")


# Include other necessary Flask routes and functions here

@app.route("/logic", methods=["POST"])
def logic():
    if request.method == "POST":
        userInput = request.form["userInput"]
        try:
            parseObject = savy_parser.Parser(userInput)
            header = parseObject.variable_list
            header.append("".join(parseObject.tokenizer(userInput)))
            truthTable = parseObject.truth_table
        except (Exception, ValueError) as err:
            errorMessage = str(err)
            return render_template("Hackathon_2024.html", errorMessage=errorMessage)
        return render_template("Hackathon_2024.html", 
                               truthTable=truthTable,
                               header=header)


if __name__ == "__main__":
    app.run(debug=True)
