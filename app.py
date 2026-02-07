from flask import Flask, render_template, request
from agent import StudyAgent

app = Flask(__name__)
agent = StudyAgent()

@app.route("/", methods=["GET", "POST"])
def index():
    output = None

    if request.method == "POST":
        subject = request.form["subject"]
        output = agent.generate_plan(subject)

    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
