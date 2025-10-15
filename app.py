from flask import Flask
#Creating a flask application
app=Flask(__name__)
@app.route("/") #Homepage route

def home():
    return "Hello,Flask!"


if __name__=="__main__":
    app.run(debug=True)