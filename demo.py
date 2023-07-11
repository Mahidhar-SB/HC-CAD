from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/hello/<string:track>") 
def hey(track):

    return f"Hello People! Welcome to HC {track} Bootcamp 1 Session"

@app.route("/")
def welcome():
    return "Welcome to the HC"

@app.route("/something")
def something():
    return "This is the new route"

@app.route("/hc/<string:anything>")
def hc(anything):

    if anything == "CAD":
        return redirect(url_for('hey', track = anything))
    else:
        return redirect(url_for('something'))


if __name__ == "__main__":
    app.run(debug=True)