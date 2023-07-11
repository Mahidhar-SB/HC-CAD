from flask import Flask, render_template, request
import ibm_db
app = Flask(__name__)

conn = conn=ibm_db.connect("DATABASE=database;HOSTNAME=hostname;PORT=port;UID=username;PWD=password;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt",'','')
print(conn)
connState = ibm_db.active(conn)
print(connState)
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        details = [name,email,password,role]
        print(details)
        sql = "SELECT * FROM REGISTER_HC where EMAILID=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        # ibm_db.bind_param(stmt, 2, name)
        ibm_db.execute(stmt)
        acc = ibm_db.fetch_assoc(stmt)
        print(acc)
        if acc:
            print("alr")
            return render_template("login.html")
        else: 
            #"code for insert values in to  "
            return render_template("profile.html")
    return render_template("profile.html")



if __name__ == "__main__":
    app.run(debug=True)