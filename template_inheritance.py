from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("extend_template.html",name="Teja")

if __name__=="__main__":
    app.run(debug=True)

