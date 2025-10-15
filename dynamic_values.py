from flask import Flask
app=Flask(__name__)



@app.route("/") #Home page
def home():
    return "Welcome to Home Page"

@app.route("/user/<name>")
def user(name):
    return f"Hello,{name}!"

@app.route("/greet/<name>/<int:age>")
def greet(name,age):
    return f"Hello {name}, you are {age} years old!"

@app.route("/square/<int:number>")
def square(number):
    result=number**2
    return f"The square of the {number} is {result}."

if __name__=="__main__":
    app.run(debug=True)