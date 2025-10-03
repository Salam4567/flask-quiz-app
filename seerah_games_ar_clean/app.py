from flask import Flask, render_template, request, session
import json
import os

app = Flask(__name__)
app.secret_key = "secret123"  # مفتاح سري للجلسة (لازم لأي استعمال للـ session)

@app.route("/")
def home():
    games_played = session.get("games_played", 0)  # اجلب قيمة العداد
    return render_template("index.html", games_played=games_played)

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    # زيادة العداد عند لعب الاختبار
    session["games_played"] = session.get("games_played", 0) + 1

    if request.method == "POST":
        # استلام الإجابات
        answers = request.form
        with open("data/questions.json", encoding="utf-8") as f:
            questions = json.load(f)

        score = 0
        details = []

        for i, q in enumerate(questions):
            user_answer = answers.get(f"q{i}")
            if user_answer == q["answer"]:
                score += 1
            details.append({
                "text": q["text"],
                "user_answer": user_answer,
                "answer": q["answer"]
            })

        return render_template("result.html", score=score, total=len(questions), details=details)

    # عرض الأسئلة
    with open("data/questions.json", encoding="utf-8") as f:
        questions = json.load(f)
    return render_template("quiz.html", questions=questions)

@app.route("/memory")
def memory():
    # زيادة العداد عند لعب لعبة الذاكرة
    session["games_played"] = session.get("games_played", 0) + 1
    return render_template("memory.html")

@app.route("/adventure")
def adventure():
    # زيادة العداد عند لعب المغامرة
    session["games_played"] = session.get("games_played", 0) + 1
    return render_template("adventure.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
