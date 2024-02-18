from flask import Flask, render_template, request, redirect, url_for
import numpy as np

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

if __name__ == "__main__":
    app.run(debug=True)
