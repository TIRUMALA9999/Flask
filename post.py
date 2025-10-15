from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return f"Welcome, {username}! (Password received securely)"
    return render_template("login.html")
if __name__=="__main__":
    app.run(debug=True)