from flask import Flask,render_template

app=Flask(__name__)

@app.route("/status/<int:age>")
def status(age):
    return render_template("status.html",age=age)


if __name__=="__main__":
    app.run(debug=True)