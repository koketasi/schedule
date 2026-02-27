from importlib.metadata import files
from flask import  render_template, request, redirect, url_for
from __init__ import app
import sqlite3
import os
from pathlib  import Path

from werkzeug.utils import secure_filename
database='database.db'

#app = Flask(__name__)

# 仮のスケジュールデータ（メモリ上）
data = []
def init_db():
    with sqlite3.connect(database) as con:
        con.execute('CREATE TABLE IF NOT EXISTS schedule1(date TEXT, event TEXT, filename TEXT, filetitle TEXT)')
        con.commit()

init_db()


@app.route('/')#, methods=["GET", "POST"])
def index():
    con=sqlite3.connect(database)
    con.execute('CREATE TABLE IF NOT EXISTS schedule1(date TEXT,event TEXT,filename TEXT,filetitle TEXT)')
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
    if request.method=='POST':
        f=request.files['gazou']
        image['gazou']=secure_filename(f.filename)
        f.save(Path(app.root_path) /"static"/ secure_filename(f.filename))

        image_title['name']=request.form['name']
        gender['sex']=request.form.get('sex')

        con=sqlite3.connect(database)
        con.execute('INSERT INTO schedule1 (filename,filetitle) VALUES(?,?)',(image['gazou'], image_title['name'],))
        con.commit()
        con.close()
    #if request.method == "POST":
    #    return redirect(url_for('form'))
    con=sqlite3.connect(database)
    file=con.execute("SELECT filename, filetitle FROM schedule1 ORDER BY rowid DESC LIMIT 1").fetchall()
    con.close()
    return render_template("form.html",gender=gender,i=file)
 


@app.route("/register",methods=['POST'])
def register():
    if request.method=='POST':
        date2=request.form['date']
        event2=request.form['event']
        con=sqlite3.connect(database)
        con.execute('INSERT INTO schedule1 (date,event)VALUES(?,?)',[date2,event2])
        con.commit()
        con.close()


    return redirect(url_for('index'))

if __name__ == "__main__":
    # Render は環境変数 PORT で指定されることが多い
    #import os
    #port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)

    
#@app.route("/debug")
#def debug():
#    files = os.listdir(os.path.join(app.root_path,"static"))
 #   return str(files)
print(os.getcwd())