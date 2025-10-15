from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home2.html")

@app.route("/greet")
def greet():
    name=request.args.get("name") 
    if name:
        return f"Hello,{name}!"
    return "Please provide a name in the URL, e.g., /greet?name=Teja"

if __name__=="__main__":
    app.run(debug=True)