from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    user="Teja"
    return render_template("home1.html",name=user)

@app.route("/users")
def users():
    people=["Alice","Bob","Charlie","Teja"]
    return render_template("loops.html",people=people)


if __name__=="__main__":
    app.run(debug=True)