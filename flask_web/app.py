from flask import Flask, render_template, request, redirect
from data import Articles
import pymysql


app = Flask(__name__)
app.debug = True
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='ekthdlek12',
    db='busan'
)


@app.route('/main', methods=['GET'])
def index():
  # return "Hello World"
  return render_template("main.html", data="KIM")


@app.route('/abt')
def about():
  return render_template("about.html", hello="Gary Kim")


@app.route('/art')
def articles():
  cursor = db.cursor()
  sql = 'SELECT * FROM topic;'
  cursor.execute(sql)
  topics = cursor.fetchall()
  # print(topics)
  # articles = Articles()
  # print(articles[0]['title'])
  return render_template("articles.html", article=topics)


@app.route('/article/<int:id>')
def article(id):
  cursor = db.cursor()
  sql = 'SELECT * FROM topic WHERE id={}'.format(id)
  cursor.execute(sql)
  topic = cursor.fetchone()  # fetchone과 fetchall의 차이
  # articles = Articles()
  # article = articles[id-1]
  return render_template("article.html", article=topic)


@app.route('/art_add', methods=["GET", "POST"])
def art_add():
  cursor = db.cursor()
  if request.method == "POST":
    title = request.form['title']
    author = request.form['author']
    desc = request.form['description']

    sql = 'INSERT INTO `topic` (`title`, `author`, `body`) VALUES (%s, %s, %s);'
    input_data = [title, author, desc]
    cursor.execute(sql, input_data)
    db.commit()
    # db.close()
    return redirect('/art')
  else:
    return render_template("art_add.html")


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
  cousour = db.cursor()
  # sql = 'DELETE FROM `topic` WHERE id = %s;'
  # id = [id]
  # cousour.execute(sql, id)
  sql = 'DELETE FROM `topic` WHERE id = {};'.format(id)
  cousour.execute(sql)
  db.commit()
  return redirect('/art')

# @app.route('/update/<int:id>')
# def update(id):
#   sql = 'DELETE FROM `topic` WHERE id = {};'.format(id)
#   cousour.execute(sql)
#   db.commit()
#   return redirect('/art')

# @app.route('/art_add', methods=['POST'])
# def art_insert():
#   # return render_template("art_add.html")
#   return "Success"
if __name__ == '__main__':
  app.run()
