from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 仮のスケジュールデータ（メモリ上）
data = []

@app.route('/', methods=["GET", "POST"])
def index():
    day={1:"アニメ",31:'自分が墓標になることだ'}

    if request.method == "POST":
        task = request.form.get("task")
        if task:  # 入力があれば追加
            data.append(task)
        return redirect(url_for("index"))
    return render_template("index.html", data=data,day=day)
@app.route('/form')
def form():
    return render_template("form.html")

if __name__ == "__main__":
    # Render は環境変数 PORT で指定されることが多い
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)