from flask import Flask, render_template, request, session
import ibm_db
app = Flask(__name__)

conn = ibm_db.connect("database=bludb;hostname=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;port=30756;uid=vts47207;pwd=g4O8mWodzytk1wMD;security=SSL;sslcertificate=DigiCertGlobalRootCA.crt"," "," ")
print(conn)
connState = ibm_db.active(conn)
print(connState)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #here you can give any random bytes


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

@app.route("/login", methods = ['GET', 'POST'])
def login():
    global uemail
    if request.method == 'POST':
        email = request.form['email']
        password =  request.form['password']
        details = [email, password]
        print(details)
        sql = "SELECT * FROM REGISTER_HC where EMAILID=? AND PASSWORD = ?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.bind_param(stmt, 2, password)
        ibm_db.execute(stmt)
        acc = ibm_db.fetch_assoc(stmt)
        print(acc)
        if acc: 
            session['email'] = email
            session['username'] = acc['NAME']
            uemail = session['email']            
            return render_template("profile.html")
        else:
            msg = "Invalid Credentials"
            return render_template("login.html", message=msg)






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
            msg = "You have been already REGISTERED, please login!"
            return render_template("login.html", message = msg)
        else: 
            sql = "INSERT into REGISTER_HC VALUES (?,?,?,?)"
            stmt = ibm_db.prepare(conn, sql)
            ibm_db.bind_param(stmt, 1, name)
            ibm_db.bind_param(stmt, 2, email)
            ibm_db.bind_param(stmt, 3, password)
            ibm_db.bind_param(stmt, 4, role)
            ibm_db.execute(stmt)
            msg = "You have Successfully REGISTERED, Please LOGIN"            
            return render_template("login.html", message = msg)
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("email", None)
    session.pop("username", None)
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)
