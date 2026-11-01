from flask import Flask, request, render_template_string
from datetime import datetime
import csv
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Card Payment Demo</title>
    <style>
        body {
            font-family: Arial;
            background: #f2f4f7;
            display: flex;
            justify-content: center;
            padding-top: 60px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
            width: 350px;
            box-shadow: 0 4px 15px #ccc;
        }
        input, button {
            box-sizing: border-box;
            width: 100%;
            padding: 12px;
            margin: 8px 0;
        }
        button {
            background: #2878e0;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
<div class="container">
    <h2>Card Payment Demo</h2>
    <p>Educational phishing-awareness simulation.
       Use fictional information only.</p>

    <form method="POST" action="/submit">
        <input name="cardholder"
               placeholder="Fictional cardholder name" required>

        <input name="demo_card"
               placeholder="Last four digits (e.g. 1234)"
               pattern="[0-9]{4}" maxlength="4" required>

        <button type="submit">Submit Demo</button>
    </form>
</div>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/submit", methods=["POST"])
def submit():
    cardholder = request.form.get("cardholder", "").strip()
    last_four = request.form.get("demo_card", "").strip()

    if not cardholder or not last_four.isdigit() or len(last_four) != 4:
        return "Invalid demo data", 400

    filename = "demo_submissions.csv"
    exists = os.path.exists(filename)

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not exists:
            writer.writerow(["Timestamp", "Cardholder", "Last Four"])

        writer.writerow([
            datetime.now().isoformat(),
            cardholder,
            last_four
        ])

    return """
    <h2>Demo submitted successfully!</h2>
    <p>This educational simulation has recorded your submission.</p>
    <a href="/">Return to demo</a>
    """


if __name__ == "__main__":
    app.run(debug=True, port=8000)