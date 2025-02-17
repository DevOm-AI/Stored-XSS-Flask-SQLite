from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY, content TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Home Page (Form to submit comments)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        comment = request.form["comment"]
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("INSERT INTO comments (content) VALUES (?)", (comment,))
        conn.commit()
        conn.close()
        return redirect("/post")
    return render_template("index.html")

# Page displaying comments (Vulnerable to Stored XSS)
@app.route("/post")
def post():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT content FROM comments")
    comments = c.fetchall()
    conn.close()
    return render_template("post.html", comments=comments)

if __name__ == "__main__":
    app.run(debug=True)

