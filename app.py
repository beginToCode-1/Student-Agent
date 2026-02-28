from flask import Flask, render_template, request
from agent import StudentAgent
from planner import generate_plan

app = Flask(__name__)

agent = StudentAgent()

@app.route("/", methods=["GET", "POST"])
def index():

    message = ""
    plan = []

    if request.method == "POST":

        action = request.form.get("action")

        # ADD TOPIC
        if action == "add":
            subject = request.form["subject"]
            topic = request.form["topic"]
            difficulty = request.form["difficulty"]

            agent.add_topic(subject, topic, difficulty)
            message = "Topic added."

        # GENERATE PLAN
        elif action == "plan":
            plan = generate_plan(agent)

        # FEEDBACK
        elif action == "feedback":
            topic = request.form["topic_feedback"]
            feedback = request.form["feedback"]

            agent.give_feedback(topic, feedback)
            message = "Feedback recorded."

        # SAVE DATA
        agent.save_data()

    return render_template(
        "index.html",
        plan=plan,
        subjects=agent.subjects,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)