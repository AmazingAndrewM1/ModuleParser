from flask import Flask
from flask import render_template, request
import savy_parser

# Assuming the Parser class and related classes are defined here or imported

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract the logical expression from the form data
        expression = request.form['userInput']

        # Initialize the Parser with the user's expression
        try:
            parser = Parser(expression)
            # Assume the parser has a method to generate a truth table as a list of dictionaries
            truth_table = parser.truth_table
        except Exception as e:
            # Handle parser errors (e.g., syntax errors in the expression)
            return render_template("index.html", error=str(e))

        # Pass the generated truth table to the template
        return render_template("index.html", truth_table=truth_table, expression=expression)
    else:
        # Initial page load (no form submission)
        return render_template("index.html")


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
