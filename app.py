from flask import Flask, render_template
app = Flask(__name__, template_folder="template")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jobbrowse")
def jobbrowse():
    return render_template("job-list.html")

@app.route("/jobpost")
def jobpost():
    return render_template("job-post.html")



if __name__ == "__main__":
    app.run(debug=True)