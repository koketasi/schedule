from importlib.metadata import files
from flask import Flask, render_template, request, redirect, url_for
from __init__ import app
import __init__
import sqlite3
import os
database='database.db'

#app = Flask(__name__)

# 仮のスケジュールデータ（メモリ上）
data = []

@app.route('/')#, methods=["GET", "POST"])
def index():
    con=sqlite3.connect(database)
    list_schedule=con.execute('select * from schedule1').fetchall()
    con.close()
    day={}
    for i in list_schedule:
        day[i[0]]=i[1]

#    day={1:"アニメ",31:'自分が墓標になることだ'}

   # if request.method == "POST":
     #   task = request.form.get("task")
      #  if task:  # 入力があれば追加
       #     data.append(task)
        
       # return redirect("/")#ボタン押したら更新?
    return render_template("index.html",day=day)

@app.route("/form",methods=['POST','GET'])
def form():
    gender={}
    image={}
    image_title={}
    f=request.files['gazou']
    image['gazou']=f.filename
    f.save(os.path.join(os.path.dirname(__file__), "static", f.filename))

    image_title['name']=request.form['name']
    gender['sex']=request.form.get('sex')
    #if request.method == "POST":
    #    return redirect(url_for('form'))
    return render_template("form.html",gender=gender,i=image,i_t=image_title)
 


@app.route("/register",methods=['POST'])
def register():
    date2=request.form['date']
    event2=request.form['event']
    con=sqlite3.connect(database)
    con.execute('INSERT INTO schedule1 VALUES(?,?)',[date2,event2])
    con.commit()
    con.close()


    return redirect(url_for('index'))

if __name__ == "__main__":
    # Render は環境変数 PORT で指定されることが多い
    #import os
    #port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)

    

print(os.getcwd())