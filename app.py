from flask import (
    Flask, render_template, request, redirect, url_for, session
)

import quiz
from data import QUESTIONS, answer_label

app = Flask(__name__)
app.secret_key = "hcde310-food-quiz"


@app.route("/")
def index():
    return render_template("index.html", has_key=quiz.has_key())


@app.route("/start", methods=["POST"])
def start():
    # begin new quiz: remember location, clear old answers
    session["location"] = request.form.get("location", "").strip() or "Seattle, WA"
    session["answers"] = {}
    return redirect(url_for("question", step=0))


@app.route("/quiz/<int:step>", methods=["GET", "POST"])
def question(step):
    # if no quiz in progresss send them back to the start
    if "answers" not in session:
        return redirect(url_for("index"))

    if step >= len(QUESTIONS):
        return redirect(url_for("results"))

    q = QUESTIONS[step]

    if request.method == "POST":
        answers = session["answers"]
        answers[q["key"]] = request.form.get(q["key"], "any")
        session["answers"] = answers
        return redirect(url_for("question", step=step + 1))

    return render_template(
        "question.html",
        question=q,
        step=step,
        total=len(QUESTIONS),
    )


@app.route("/results")
def results():
    if "answers" not in session:
        return redirect(url_for("index"))

    answers = session["answers"]
    location = session.get("location", "Seattle, WA")

    picks = quiz.recommend(answers)
    cards = [
        {"food": food, "restaurants": quiz.get_restaurants(food["search"], location)}
        for food in picks
    ]

    chosen = [
        answer_label(q["key"], answers[q["key"]])
        for q in QUESTIONS
        if answers.get(q["key"], "any") != "any"
    ]

    return render_template(
        "results.html",
        cards=cards,
        location=location,
        chosen=chosen,
        has_key=quiz.has_key(),
    )


if __name__ == "__main__":
    app.run(debug=True)