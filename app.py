from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 仮のスケジュールデータ（メモリ上）
schedule = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:  # 入力があれば追加
            schedule.append(task)
        return redirect(url_for("index"))
    return render_template("index.html", schedule=schedule)

if __name__ == "__main__":
    # Render は環境変数 PORT で指定されることが多い
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)