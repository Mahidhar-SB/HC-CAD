from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jobbrowse")
def jobbrowse():
    return render_template("job-list.html")

@app.route("/jobpost")
def jobpost():
    return render_template("job-post.html")

@app.route("/jobview")
def jobview():
    return render_template("job-view.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")



if __name__ == "__main__":
    app.run(debug=True)